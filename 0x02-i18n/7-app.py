#!/usr/bin/env python3
"""flask instance"""
import pytz
from typing import Optional, Dict
from flask_babel import Babel
from pytz.exceptions import UnknownTimeZoneError
from flask import Flask, render_template, request, g


app = Flask(__name__)
babel = Babel(app)


class Config:
    """configure langs"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[Dict]:
    """getting user id"""
    try:
        get_id = int(request.args.get('login_as'))
        data = users.get(get_id)
        return data
    except Exception:
        return None


@app.before_request
def before_request() -> None:
    """setting to global var"""
    g.user = get_user()


@babel.timezoneselector
def get_timezone() -> str:
    """get user timezone"""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone).zone
        except UnknownTimeZoneError:
            pass
    if g.user and g.user['timezone']:
        try:
            return pytz.timezone(g.user['timezone']).zone
        except UnknownTimeZoneError:
            pass
    return 'UTC'


@babel.localeselector
def get_locale() -> str:
    """get locale"""
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']

    return "request.accept_languages.best_match(app.config['LANGUAGES'])"


@app.route("/")
def index() -> str:
    """return template"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
