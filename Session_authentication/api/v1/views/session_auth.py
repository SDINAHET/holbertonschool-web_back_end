#!/usr/bin/env python3
"""
New route for Session Authentication
Handles POST /api/v1/auth_session/login
"""

from flask import request, jsonify, make_response
from flasgger.utils import swag_from
from flask import abort  #task8
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
@swag_from({
    'tags': ['Session Authentication'],
    'summary': 'Create session and return user info',
    'description': (
        'Authenticates a user using email and password, '
        'and sets session cookie.'
    ),
    'parameters': [
        {
            'name': 'email',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'User email'
        },
        {
            'name': 'password',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'User password'
        }
    ],
    'responses': {
        200: {
            'description': 'User authenticated, session created',
            'examples': {
                'application/json': {
                    "id": "cf3ddee1-ff24-49e4-a40b-2540333fe992",
                    "email": "bobsession@hbtn.io",
                    "first_name": None,
                    "last_name": None,
                    "created_at": "2017-10-16 04:23:04",
                    "updated_at": "2017-10-16 04:23:04"
                }
            }
        },
        400: {
            'description': 'Missing email or password'
        },
        401: {
            'description': 'Wrong password'
        },
        404: {
            'description': 'User not found'
        }
    }
})
def session_login():
    """
    Handles session login: validates email/password, creates session,
    sets session cookie, returns user JSON.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # 👇 Importer auth ici pour éviter l'import circulaire
    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    response = make_response(jsonify(user.to_json()))
    session_name = getenv("SESSION_NAME")
    response.set_cookie(session_name, session_id)

    return response

@app_views.route(
    '/auth_session/logout',
    methods=['DELETE'],
    strict_slashes=False
)
@swag_from({
    'tags': ['Session Authentication'],
    'summary': 'Logout user by destroying session',
    'description': 'Deletes the session cookie to log out the user.',
    'responses': {
        200: {
            'description': 'Session successfully destroyed',
            'examples': {
                'application/json': {}
            }
        },
        404: {
            'description': 'Session not found or invalid'
        }
    }
})
def session_logout():
    """
    Logs out a user by destroying the session ID from the cookie.
    """
    from api.v1.app import auth  # éviter l'import circulaire
    destroyed = auth.destroy_session(request)

    if not destroyed:
        abort(404)

    return jsonify({}), 200
