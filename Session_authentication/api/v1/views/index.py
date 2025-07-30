#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views
from flasgger.utils import swag_from  # ✅ Import pour Swagger
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
@swag_from({
    'tags': ['Status'],
    'responses': {
        200: {
            'description': 'Return API status',
            'examples': {
                'application/json': {
                    'status': 'OK'
                }
            }
        }
    }
})
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
@swag_from({
    'tags': ['Statistics'],
    'summary': 'Get total count of each object',
    'description': 'Returns the number of objects stored by model (e.g., users, places, etc.)',
    'responses': {
        200: {
            'description': 'A JSON dictionary with object counts',
            'content': {
                'application/json': {
                    'example': {
                        'users': 42
                    }
                }
            }
        }
    }
})
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
@swag_from({
    'tags': ['Errors'],
    'summary': 'Force a 401 Unauthorized error',
    'description': 'This route is used to simulate a 401 Unauthorized error.',
    'responses': {
        401: {
            'description': 'Unauthorized - authentication is required and has failed or has not yet been provided.',
            'content': {
                'application/json': {
                    'example': {
                        'error': 'Unauthorized'
                    }
                }
            }
        }
    }
})
def raise_unauthorized():
    """ Raise 401 Unauthorized error """
    abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
@swag_from({
    'tags': ['Errors'],
    'summary': 'Force a 403 Forbidden error',
    'description': 'This route simulates a 403 Forbidden error, indicating that the user is authenticated but does not have permission.',
    'responses': {
        403: {
            'description': 'Forbidden - the server understood the request but refuses to authorize it.',
            'content': {
                'application/json': {
                    'example': {
                        'error': 'Forbidden'
                    }
                }
            }
        }
    }
})
def raise_forbidden():
    """ GET /api/v1/forbidden - Raise a 403 Forbidden error """
    abort(403)
