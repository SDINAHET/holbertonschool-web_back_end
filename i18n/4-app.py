#!/usr/bin/env python3
"""
Flask app: force locale via URL parameter with Flask-Babel.

- Supports locales: en, fr
- If a request has ?locale=fr|en, use it; otherwise use Accept-Language.
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Application configuration for Flask-Babel.

    Attributes:
        LANGUAGES (list[str]): Supported locales.
        BABEL_DEFAULT_LOCALE (str): Fallback locale when no match is found.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()


def get_locale():
    """
    Locale selector: URL param takes precedence, else Accept-Language.

    Returns:
        str | None: Selected locale among supported languages.
    """
    # 1) Force from URL ?locale=...
    forced = request.args.get("locale", type=str)
    if forced and forced in app.config["LANGUAGES"]:
        return forced
    # 2) Fallback to best match from headers
    return request.accept_languages.best_match(app.config["LANGUAGES"])


# Bind Babel with our selector
babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """Render translated home page for step 4."""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
