#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from flasgger.utils import swag_from


@app_views.route('/users', methods=['GET'], strict_slashes=False)
@swag_from({
    'tags': ['Users'],
    'summary': 'Get all users',
    'responses': {
        200: {
            'description': 'List of all users',
            'schema': {
                'type': 'array',
                'items': {
                    '$ref': '#/definitions/User'
                }
            }
        }
    }
})
def view_all_users() -> str:
    """ GET /api/v1/users
    Return:
      - list of all User objects JSON represented
    """
    all_users = [user.to_json() for user in User.all()]
    return jsonify(all_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
@swag_from({
    'tags': ['Users'],
    'summary': 'Get user by ID or "me"',
    'parameters': [
        {
            'name': 'user_id',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': 'User ID or "me"'
        }
    ],
    'responses': {
        200: {
            'description': 'User found',
            'schema': {
                '$ref': '#/definitions/User'
            }
        },
        404: {
            'description': 'User not found'
        }
    }
})
def view_one_user(user_id: str = None) -> str:
    """
    GET /api/v1/users/<user_id> or /users/me
    Path parameter:
      - User ID or the string "me"
    Return:
      - User object JSON represented
      - 404 if the User ID doesn't exist or if "me" is used and user is not
      authenticated
    """
    if user_id is None:
        abort(404)

    if user_id == "me":
        if not hasattr(request, "current_user") or \
                request.current_user is None:
            abort(404)
        return jsonify(request.current_user.to_json())

    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_json())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
@swag_from({
    'tags': ['Users'],
    'summary': 'Delete a user by ID',
    'parameters': [
        {
            'name': 'user_id',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': 'User ID'
        }
    ],
    'responses': {
        200: {
            'description': 'User deleted successfully',
            'schema': {
                'type': 'object'
            }
        },
        404: {
            'description': 'User not found'
        }
    }
})
def delete_user(user_id: str = None) -> str:
    """ DELETE /api/v1/users/:id
    Path parameter:
      - User ID
    Return:
      - empty JSON is the User has been correctly deleted
      - 404 if the User ID doesn't exist
    """
    if user_id is None:
        abort(404)
    user = User.get(user_id)
    if user is None:
        abort(404)
    user.remove()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
@swag_from({
    'tags': ['Users'],
    'summary': 'Create a new user',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {'type': 'string'},
                    'password': {'type': 'string'},
                    'first_name': {'type': 'string'},
                    'last_name': {'type': 'string'}
                },
                'required': ['email', 'password']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'User created',
            'schema': {
                '$ref': '#/definitions/User'
            }
        },
        400: {
            'description': 'Invalid input'
        }
    }
})
def create_user() -> str:
    """ POST /api/v1/users/
    JSON body:
      - email
      - password
      - last_name (optional)
      - first_name (optional)
    Return:
      - User object JSON represented
      - 400 if can't create the new User
    """
    rj = None
    error_msg = None
    try:
        rj = request.get_json()
    except Exception as e:
        rj = None
    if rj is None:
        error_msg = "Wrong format"
    if error_msg is None and rj.get("email", "") == "":
        error_msg = "email missing"
    if error_msg is None and rj.get("password", "") == "":
        error_msg = "password missing"
    if error_msg is None:
        try:
            user = User()
            user.email = rj.get("email")
            user.password = rj.get("password")
            user.first_name = rj.get("first_name")
            user.last_name = rj.get("last_name")
            user.save()
            return jsonify(user.to_json()), 201
        except Exception as e:
            error_msg = "Can't create User: {}".format(e)
    return jsonify({'error': error_msg}), 400


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
@swag_from({
    'tags': ['Users'],
    'summary': 'Update a user by ID',
    'parameters': [
        {
            'name': 'user_id',
            'in': 'path',
            'type': 'string',
            'required': True
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'first_name': {'type': 'string'},
                    'last_name': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'User updated successfully',
            'schema': {
                '$ref': '#/definitions/User'
            }
        },
        400: {
            'description': 'Invalid input format'
        },
        404: {
            'description': 'User not found'
        }
    }
})
def update_user(user_id: str = None) -> str:
    """ PUT /api/v1/users/:id
    Path parameter:
      - User ID
    JSON body:
      - last_name (optional)
      - first_name (optional)
    Return:
      - User object JSON represented
      - 404 if the User ID doesn't exist
      - 400 if can't update the User
    """
    if user_id is None:
        abort(404)
    user = User.get(user_id)
    if user is None:
        abort(404)
    rj = None
    try:
        rj = request.get_json()
    except Exception as e:
        rj = None
    if rj is None:
        return jsonify({'error': "Wrong format"}), 400
    if rj.get('first_name') is not None:
        user.first_name = rj.get('first_name')
    if rj.get('last_name') is not None:
        user.last_name = rj.get('last_name')
    user.save()
    return jsonify(user.to_json()), 200
