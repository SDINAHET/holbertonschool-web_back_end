#!/usr/bin/env python3
"""
Route module for the API
Sets up the Flask app and registers blueprints, error handlers, and CORS.
"""

from os import getenv
from flask import Flask, jsonify
from flask_cors import CORS
from api.v1.views import app_views

app = Flask(__name__)

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


if __name__ == "__main__":
    # Load host and port from environment or use default
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))
    app.run(host=host, port=port)
