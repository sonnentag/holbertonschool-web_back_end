#!/usr/bin/env python3
"""
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz.exceptions
from pytz import timezone


app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def hello():
    """ Hello method.
    """
    return render_template('index.html')


@babel.localeselector
def get_locale():
    """
    """
    locale = request.args.get('locale')
    reqHeader = request.args.get('locale')
    languages = app.config['LANGUAGES']

    if locale:
        if locale in languages:
            return locale
    else:
        try:
            userParam = g.user.locale
        except Exception:
            userParam = None

    if userParam and userParam in languages:
        return userParam
    elif reqHeader and reqHeader in languages:
        return reqHeader

    return request.accept_languages.best_match(languages)


@babel.timezoneselector
def get_timezone():
    """ Infer appropriate time zone
    """
    tzParam = request.args.get('timezone')
    tzUser = g.user.timezone

    try:
        if tzParam:
            return tzParam
        elif tzUser:
            return tzUser
        return pytz.utc
    except pytz.exceptions.UnknownTimeZoneError:
        return pytz.utc


@app.before_request
def before_request():
    """ before request
    """
    g.user = get_user()


def get_user():
    """
    """
    try:
        return users.get(int(request.args.get("login_as")))
    except Exception:
        return None


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
