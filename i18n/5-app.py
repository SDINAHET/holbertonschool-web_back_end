#!/usr/bin/env python3
"""
Flask app: mock login + translated messages.

- Mock users via ?login_as=<id>
- Store current user in flask.g.user (or None)
- Force locale via ?locale=fr|en, else use Accept-Language
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """
    Application configuration for Flask-Babel.

    Attributes:
        LANGUAGES (list[str]): Supported locales.
        BABEL_DEFAULT_LOCALE (str): Fallback locale.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Mock "database" of users
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()


def get_locale():
    """
    Locale selector: URL param takes precedence, else Accept-Language.
    """
    forced = request.args.get("locale", type=str)
    if forced in app.config["LANGUAGES"]:
        return forced
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


def get_user():
    """
    Return the mocked user dict from ?login_as=<id>, or None.
    """
    uid = request.args.get("login_as", type=int)
    if uid and uid in users:
        return users[uid]
    return None


@app.before_request
def before_request():
    """
    Run before each request. Attach current user (if any) to flask.g.
    """
    g.user = get_user()


@app.route("/")
def index():
    """
    Render translated home page for step 5.
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
