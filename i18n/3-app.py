#!/usr/bin/env python3
"""
Flask app: parametrized templates with Flask-Babel
"""
from flask import Flask, render_template, request
from flask_babel import Babel

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()

def get_locale():
    return request.accept_languages.best_match(app.config["LANGUAGES"])

babel.init_app(app, locale_selector=get_locale)

@app.route("/")
def index():
    return render_template("3-index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
