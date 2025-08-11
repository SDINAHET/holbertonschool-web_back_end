#!/usr/bin/env python3
"""
Flask app: detect locale from request using Flask-Babel
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration for Babel and available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()  # create Babel instance without binding


def get_locale():
    """Select the best match between client's Accept-Language and supported
    LANGUAGES."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


# Initialize Babel with our locale selector
babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """Render the index page"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
