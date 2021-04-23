#!/usr/bin/env python3
""" 5. Mock logging in
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ configure available languages
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def hello():
    """ Hello method.
    """
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """ determine the best match with our supported languages
    """
    locale = request.args.get('locale')
    languages = app.config['LANGUAGES']
    if locale in languages:
        return locale
    return request.accept_languages.best_match(languages)


@app.before_request
def before_request():
    """ before request
    """
    g.user = get_user()


def get_user():
    """ get user dict
    """
    try:
        return users.get(int(request.args.get("login_as")))
    except Exception:
        return None


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
