#!/usr/bin/env python3
"""  Module for SessAuth views
"""
from api.v1.views import app_views, auth
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ All routes for SessionAuth
    """
    email = request.form.get('email')
    passwordd = request.form.get('password')
    if not email:
        return make_response(jsonify({"error": "email missing"}), 400)
    if not password:
        return make_response(jsonify({"error": "password missing"}), 400)

    user_instrance = User.search({"email": email})
    if len(user_instance) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    for user in user_instance:
        if (user.is_valid_password(password)):
            session_id = auth.create_session(user.id)
            session_name = getenv('SESSION_NAME')
            response = make_response(user.to_json())
            response.set_cookie(session_name, session_id)
            return response

    return make_response(jsonify({"error": "wrong password"}), 401)


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout():
    """ Logout session
    """
    dest_request = auth.destroy_session(request)

    if dest_request:
        return jsonify({}), 200
    abort(404)
