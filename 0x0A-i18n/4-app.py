#!/usr/bin/env python3
""" 4. Force locale with URL parameter
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


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
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """ determine the best match with our supported languages
    """
    locale = request.args.get('locale')
    languages = app.config['LANGUAGES']
    if locale in languages:
        return locale
    return request.accept_languages.best_match(languages)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
