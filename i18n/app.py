#!/usr/bin/env python3
"""
Flask app (step 8): display current time with locale & timezone.
"""
from datetime import datetime
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz
from pytz.exceptions import UnknownTimeZoneError


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Mock users
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()


def get_user():
    uid = request.args.get("login_as", type=int)
    return users.get(uid) if uid in users else None


@app.before_request
def before_request():
    g.user = get_user()


def get_locale():
    # 1) URL
    forced = request.args.get("locale", type=str)
    if forced in app.config["LANGUAGES"]:
        return forced
    # 2) User
    if g.get("user"):
        uloc = g.user.get("locale")
        if uloc in app.config["LANGUAGES"]:
            return uloc
    # 3) Header
    match = request.accept_languages.best_match(app.config["LANGUAGES"])
    if match:
        return match
    # 4) Default
    return app.config["BABEL_DEFAULT_LOCALE"]


def get_timezone():
    # 1) URL
    tz = request.args.get("timezone", type=str)
    if tz:
        try:
            pytz.timezone(tz)
            return tz
        except UnknownTimeZoneError:
            pass
    # 2) User
    if g.get("user"):
        utz = g.user.get("timezone")
        if utz:
            try:
                pytz.timezone(utz)
                return utz
            except UnknownTimeZoneError:
                pass
    # 3) Default
    return app.config["BABEL_DEFAULT_TIMEZONE"]


babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route("/")
def index():
    """
    Render the home page with current localized time.
    """
    now_utc = datetime.utcnow()  # naive UTC datetime
    # format_datetime utilisera locale + timezone sélectionnés par Babel
    current_time = format_datetime(now_utc)
    return render_template("index.html", current_time=current_time)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
