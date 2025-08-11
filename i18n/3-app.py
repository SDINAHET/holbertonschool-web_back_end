#!/usr/bin/env python3
"""
Flask app: parametrized templates with Flask-Babel
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Application configuration for Flask-Babel.

    Attributes:
        LANGUAGES (list[str]): List of supported locales (e.g., ["en", "fr"]).
        BABEL_DEFAULT_LOCALE (str): Fallback locale when no match is found.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone used by Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()


def get_locale():
    """
    Select the best-matching locale from the client's Accept-Language header.

    Returns:
        str | None: The best match among supported languages, or None.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """
    Render the translated home page.

    Returns:
        str: Rendered HTML of templates/3-index.html.
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
