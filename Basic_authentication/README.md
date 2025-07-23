📡 Basic Authentication - Holberton School Project

# Simple API

Simple HTTP API for playing with `User` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)


Project level: Amateur
Directory: Basic_authentication

📚 Description

In this project, you will build and understand a Basic Authentication system from scratch, using Python and Flask.

⚠️ Note: In a production environment, you should never implement your own authentication system. Instead, use existing and battle-tested libraries like Flask-HTTPAuth. This project is for educational purposes.

🎯 Learning Objectives

After completing this project, you should be able to explain:

What authentication means

What Base64 encoding is

How to encode/decode a string using Base64

What Basic Authentication is

How the Authorization HTTP header works

📦 Resources

REST API Authentication Mechanisms

Base64 in Python

HTTP Authorization Header

Flask documentation

⚙️ Requirements

Python Scripts

Python 3.9 - Ubuntu 20.04 LTS

Files must end with a newline

All scripts must start with #!/usr/bin/env python3

PEP 8 (pycodestyle 2.5)

Executable scripts

Use of wc to verify file length

Documentation

Each module, class, and function must be documented with real sentences.

🚀 Getting Started

1. Setup and Run the API

pip3 install -r requirements.txt
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app

Test in another terminal:

curl http://0.0.0.0:5000/api/v1/status

Response:

{"status": "OK"}

✅ Tasks Overview

1. Error handler: 401 Unauthorized

Add error handler in api/v1/app.py

Custom endpoint /api/v1/unauthorized that raises 401 using abort()

2. Error handler: 403 Forbidden

Add error handler for 403

Endpoint /api/v1/forbidden using abort(403)

3. Auth class

Create Auth class with methods:

require_auth()

authorization_header()

current_user()

4. Define public routes

Update require_auth() to ignore excluded paths (slash-tolerant)

5. Request validation

Validate Authorization header presence

Use before_request to apply checks

Abort 401 or 403 accordingly

6. BasicAuth class

Create BasicAuth subclass of Auth

Load based on AUTH_TYPE=basic_auth

7. Extract Base64 from header

extract_base64_authorization_header() in BasicAuth

8. Decode Base64 value

decode_base64_authorization_header() to decode the header

9. Extract user credentials

extract_user_credentials() splits decoded string into email/password

Support passwords with :

10. Match credentials to user

user_object_from_credentials() checks DB and password validity

11. Full current_user implementation

Implement final current_user() by chaining previous methods

12. Support : in passwords

Update extract_user_credentials() to split only at first :

13. Wildcard exclusion support

Allow * at end of excluded paths for prefix-matching

🧪 Usage Examples

curl -H "Authorization: Basic <Base64>" http://0.0.0.0:5000/api/v1/users

Returns authenticated user's data if valid.

📁 Repository Structure

Basic_authentication/
├── api/
│   └── v1/
│       ├── app.py
│       ├── views/
│       │   └── index.py
│       └── auth/
│           ├── __init__.py
│           ├── auth.py
│           └── basic_auth.py
├── models/
│   └── user.py
├── main_0.py .. main_6.py
├── main_100.py
└── requirements.txt



Inspired by real-world authentication systems.

🔐 Reminder

In production, always use tested and secure solutions like Flask-HTTPAuth, OAuth2, or JWT. This project is for educational purposes only.

🔗 Related Projects

0x01. Personal Data

0x02. Session Authentication
