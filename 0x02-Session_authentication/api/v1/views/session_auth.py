#!/usr/bin/env python3
"""
    Module of Session Authentication
    """


from api.v1.views import app_views
from flask import abort, jsonify, request, session, make_response
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def create_session() -> str:
    """
    POST /api/v1/auth_session/login
    JSON body:
      - email
      - password
    Return:
      - User JSON object with session cookie if login is successful
      - 400 if email or password is missing
      - 404 if no user is found for the given email
      - 401 if the password is incorrect
    """
    email = request.form.get('email')
    if not email:
        return jsonify({'error': 'email missing'}), 400
    password = request.form.get('password')
    if not password:
        return jsonify({'error': 'password missing'}), 400
    user = User.search({'email': email})
    if not user:
        return jsonify({'error': 'no user found for this email'}), 404

    if not user.is_valid_password(password):
        return jsonify({'error': 'wrong password'}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    session_name = os.getenv('SESSION_NAME', 'session_id')
    user_json = user.to_json()
    res = make_response(jsonify(user_json))
    res.set_cookie(session_name, session_id)
    return res


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def destroy_session() -> str:
    """
    DELETE /api/v1/auth_session/logout
    Return:
      - Empty JSON object
      - 404 if session cannot be found
    """

    from api.v1.app import auth
    if auth.destroy_session(request) is False:
        abort(404)
    return jsonify({}), 200
