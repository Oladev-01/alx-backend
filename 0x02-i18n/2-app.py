#!/usr/bin/env python3
"""flask instance"""
from flask_babel import Babel
from flask import Flask, render_template, request

app = Flask(__name__)


class Config:
    """configure langs"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """get locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index() -> str:
    """return template"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
