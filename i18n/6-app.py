#!/usr/bin/env python3
"""
Flask app: locale priority (URL > user setting > headers > default).

- Mock users via ?login_as=<id>
- Store current user in flask.g.user
- Locale selection order:
  1) ?locale=fr|en
  2) g.user["locale"] if supported
  3) Accept-Language best match
  4) Default ("en")
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """
    App config for Flask-Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Mock users database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},  # invalid/unsu
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()


def get_user():
    """
    Return mocked user dict from ?login_as=<id>, else None.
    """
    uid = request.args.get("login_as", type=int)
    return users.get(uid) if uid in users else None


@app.before_request
def before_request():
    """
    Attach current user to flask.g for this request.
    """
    g.user = get_user()


def get_locale():
    """
    Locale selector with priority:
    URL param -> user setting -> Accept-Language -> default.
    """
    # 1) URL param
    forced = request.args.get("locale", type=str)
    if forced in app.config["LANGUAGES"]:
        return forced

    # 2) User setting
    user = getattr(g, "user", None)
    if user:
        uloc = user.get("locale")
        if uloc in app.config["LANGUAGES"]:
            return uloc

    # 3) Accept-Language header
    match = request.accept_languages.best_match(app.config["LANGUAGES"])
    if match:
        return match

    # 4) Default
    return app.config["BABEL_DEFAULT_LOCALE"]


# Bind Babel with our selector
babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """
    Render translated home page for step 6.
    """
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
