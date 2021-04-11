#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None

if os.getenv('AUTH_TYPE') == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif os.getenv('AUTH_TYPE') == 'session_auth':
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.before_request
def before_request() -> str:
    """ Before request handler
    """
    path_list = ['/api/v1/status/',
                 '/api/v1/unauthorized/',
                 '/api/v1/forbidden/']
    if not auth or not auth.require_auth(request.path, path_list):
        return None

    if auth.authorization_header(request) is None:
        abort(401)
    if auth.current_user(request) is None:
        abort(403)

    request.current_user = auth.current_user(request)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(403)
def not_allowed(error) -> str:
    """ Not allowed/forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(401)
def not_authorized(error) -> str:
    """ Not authorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)