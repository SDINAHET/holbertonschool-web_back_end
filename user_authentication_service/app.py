#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify, request, abort, redirect
from flasgger import Swagger
from auth import Auth

app = Flask(__name__)
AUTH = Auth()

# (Optionnel) Métadonnées OpenAPI
# swagger = Swagger(app, template={
#     "swagger": "2.0",
#     "info": {
#         "title": "My Flask API",
#         "description": "Simple API with Swagger UI (Flasgger)",
#         "version": "1.0.0"
#     },
#     "basePath": "/",
#     "schemes": ["http"]
# })

app.config["SWAGGER"] = {
    "title": "My Flask API",
    "uiversion": 3,
}
Swagger(app, template={
    "swagger": "2.0",
    "info": {"title": "My Flask API", "version": "1.0.0"},
    "basePath": "/",
    "schemes": ["http"],
    "tags": [
        {"name": "Root", "description": "General endpoints"},
        {"name": "Auth", "description": "Authentication endpoints"},
    ],
    # 👉 clé pour afficher le bouton "Authorize"
    "securityDefinitions": {
        "CookieAuth": {
            "type": "apiKey",
            "name": "Cookie",   # on passera "session_id=<uuid>"
            "in": "header"
        }
    }
})


@app.route("/", methods=["GET"])
def index():
    """
    Index endpoint
    ---
    tags:
      - Root
    summary: Welcome message
    description: Returns a JSON message welcoming the user to the API.
    produces:
      - application/json
    responses:
      200:
        description: A welcome message
        schema:
          type: object
          properties:
            message:
              type: string
              example: Bienvenue
    """
    # """GET / route - retourne un message JSON"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    """
    Register a new user
    ---
    tags: [Auth]
    consumes:
      - application/x-www-form-urlencoded
    parameters:
      - in: formData
        name: email
        type: string
        required: true
        description: User email
      - in: formData
        name: password
        type: string
        required: true
        description: User password
    responses:
      200:
        description: User created
        schema:
          type: object
          properties:
            email: {type: string, example: bob@me.com}
            message: {type: string, example: user created}
      400:
        description: Email already registered or missing fields
        schema:
          type: object
          properties:
            message: {type: string, example: email already registered}
    """
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def login():
    """
    Log in user and create a session
    ---
    tags:
      - Auth
    consumes:
      - application/x-www-form-urlencoded
    parameters:
      - in: formData
        name: email
        type: string
        required: true
        description: User email
      - in: formData
        name: password
        type: string
        required: true
        description: User password
    responses:
      200:
        description: Login successful, session created
        schema:
          type: object
          properties:
            email:
              type: string
              example: bob@bob.com
            message:
              type: string
              example: logged in
        headers:
          Set-Cookie:
            description: Session cookie
            type: string
            example: session_id=163fe508-19a2-48ed-a7c8-d9c6e56fabd1; Path=/
      401:
        description: Unauthorized (invalid credentials)
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password or not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    if session_id is None:
        abort(401)

    resp = jsonify({"email": email, "message": "logged in"})
    resp.set_cookie("session_id", session_id, path="/")
    return resp


@app.route("/sessions", methods=["DELETE"])
def logout():
    """
    Log out (destroy session)
    ---
    tags: [Auth]
    parameters:
      - in: header
        name: Cookie
        type: string
        required: true
        description: "Session cookie: session_id=<uuid>"
        default: "session_id=11111111-1111-1111-1111-111111111111"
    responses:
      302:
        description: Redirects to /
      403:
        description: Forbidden (no valid session)
    """
    # """
    # Log out (destroy session)
    # ---
    # tags: [Auth]
    # summary: Logout user and destroy session
    # responses:
    #   302:
    #     description: Redirects to /
    #   403:
    #     description: Forbidden (no valid session)
    # """
    session_id = request.cookies.get("session_id")
    if not session_id:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)
    # Redirection 302 par défaut vers la racine
    return redirect("/")


@app.route("/profile", methods=["GET"])
def profile():
    """
    Get user profile by session cookie
    ---
    tags: [Auth]
    parameters:
      - in: header
        name: Cookie
        type: string
        required: true
        description: "Session cookie: session_id=<uuid>"
        default: "session_id=11111111-1111-1111-1111-111111111111"
    responses:
      200:
        description: Profile found
        schema:
          type: object
          properties:
            email:
              type: string
              example: bob@bob.com
      403:
        description: Forbidden (invalid or missing session)
    """
    # """
    # Get user profile by session cookie
    # ---
    # tags: [Auth]
    # responses:
    #   200:
    #     description: Profile found
    #     schema:
    #       type: object
    #       properties:
    #         email:
    #           type: string
    #           example: bob@bob.com
    #   403:
    #     description: Forbidden (invalid or missing session)
    # """
    session_id = request.cookies.get("session_id")
    if not session_id:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)

    return jsonify({"email": user.email}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
