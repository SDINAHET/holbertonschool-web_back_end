#!/usr/bin/env python3
"""
Route module for the API
Sets up the Flask app and registers blueprints, error handlers, and CORS.
"""

from os import getenv
from flask import Flask, jsonify
from flask_cors import CORS
from api.v1.views import app_views
# from api.v1.auth.auth import Auth
from flask import abort, request
from flasgger import Swagger  # ✅ Ajout Swagger

auth = None
auth_type = getenv("AUTH_TYPE")

if auth_type == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()
elif auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth_type == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()

app = Flask(__name__)

app.config['SWAGGER'] = {
    'title': 'Session storage API',
    'uiversion': 3
}
swagger = Swagger(app)  # Initialise Flasgger avec l'app Flask


# Register blueprints
app.register_blueprint(app_views)

# Enable CORS for all /api/v1/* routes
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


# Custom error handler for 404
@app.errorhandler(404)
def not_found(error) -> str:
    """ Return a JSON-formatted 404 error """
    return jsonify({"error": "Not found"}), 404


# Custom error handler for 401
@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Return a JSON-formatted 401 error """
    return jsonify({"error": "Unauthorized"}), 401


# Custom error handler for 403
@app.errorhandler(403)
def forbidden(error) -> str:
    """ Return a JSON-formatted 403 error """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request_func():
    """
    Validates all requests before they reach route handlers
    """
    if auth is None:
        return
    excluded_paths = [
        '/api/v1/status/', '/api/v1/status',
        '/api/v1/unauthorized/', '/api/v1/unauthorized',
        '/api/v1/forbidden/', '/api/v1/forbidden',
        '/apidocs', '/apidocs/', '/apispec_1.json',  # Swagger UI
        '/api/v1/auth_session/login/',  # 👈 AJOUT task5
    ]

    # ✅ Autoriser Swagger static + spec JSON
    if request.path.startswith('/flasgger_static/'):
        return

    # ✅ Autoriser explicitement la spec JSON Swagger
    if request.path == '/apispec_1.json':
        return

    if not auth.require_auth(request.path, excluded_paths):
        return

    # if auth.authorization_header(request) is None:
    #     abort(401)
    if auth.authorization_header(request) is None and auth.session_cookie(request) is None:
        abort(401)


    user = auth.current_user(request)  # ✅ Tu avais oublié cette ligne
    if user is None:
        abort(403)
    request.current_user = user  # ✅


if __name__ == "__main__":
    # Load host and port from environment or use default
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))
    app.run(host=host, port=port)
