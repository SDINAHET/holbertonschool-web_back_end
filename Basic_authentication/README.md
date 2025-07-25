# 📡 Basic Authentication - Holberton School Project
```bash
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```


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

## 📚 Description

In this project, you will build and understand a Basic Authentication system from scratch, using Python and Flask.

## ⚠️ Note: In a production environment, you should never implement your own authentication system. Instead, use existing and battle-tested libraries like Flask-HTTPAuth. This project is for educational purposes.

## 🎯 Learning Objectives

After completing this project, you should be able to explain:

What authentication means

What Base64 encoding is

How to encode/decode a string using Base64

What Basic Authentication is

How the Authorization HTTP header works

## 📦 Resources

REST API Authentication Mechanisms

Base64 in Python

HTTP Authorization Header

Flask documentation

## ⚙️ Requirements

Python Scripts

Python 3.9 - Ubuntu 20.04 LTS

Files must end with a newline

All scripts must start with #!/usr/bin/env python3

PEP 8 (pycodestyle 2.5)

Executable scripts

Use of wc to verify file length

Documentation

Each module, class, and function must be documented with real sentences.

## 🚀 Getting Started

### 1. Setup and Run the API

```python
pip3 install -r requirements.txt
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

Test in another terminal:
```bash
curl http://0.0.0.0:5000/api/v1/status
```
Response:

{"status": "OK"}

✅ Tasks Overview

#### 1. Error handler: 401 Unauthorized

Add error handler in api/v1/app.py

Custom endpoint /api/v1/unauthorized that raises 401 using abort()

#### 2. Error handler: 403 Forbidden

Add error handler for 403

Endpoint /api/v1/forbidden using abort(403)

#### 3. Auth class

Create Auth class with methods:

require_auth()

authorization_header()

current_user()

#### 4. Define public routes

Update require_auth() to ignore excluded paths (slash-tolerant)

#### 5. Request validation

Validate Authorization header presence

Use before_request to apply checks

Abort 401 or 403 accordingly

#### 6. BasicAuth class

Create BasicAuth subclass of Auth

Load based on AUTH_TYPE=basic_auth

#### 7. Extract Base64 from header

extract_base64_authorization_header() in BasicAuth

#### 8. Decode Base64 value

decode_base64_authorization_header() to decode the header

#### 9. Extract user credentials

extract_user_credentials() splits decoded string into email/password

Support passwords with :

#### 10. Match credentials to user

user_object_from_credentials() checks DB and password validity

#### 11. Full current_user implementation

Implement final current_user() by chaining previous methods

#### 12. Support : in passwords

Update extract_user_credentials() to split only at first :

#### 13. Wildcard exclusion support

Allow * at end of excluded paths for prefix-matching

## 🧪 Usage Examples
```bash
curl -H "Authorization: Basic <Base64>" http://0.0.0.0:5000/api/v1/users
```

Returns authenticated user's data if valid.

## 📁 Repository Structure

```plaintext
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
```


Inspired by real-world authentication systems.

## 🔐 Reminder

In production, always use tested and secure solutions like Flask-HTTPAuth, OAuth2, or JWT. This project is for educational purposes only.

## 🔗 Related Projects

0x01. Personal Data

0x02. Session Authentication


### Task0
app.py:
```python
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

if __name__ == "__main__":
    # Load host and port from environment or use default
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))
    app.run(host=host, port=port)
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/status" -vvv
*   Trying 0.0.0.0:5000...
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/status HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.81.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 16
< Access-Control-Allow-Origin: *
< Server: Werkzeug/1.0.1 Python/3.10.12
< Date: Wed, 23 Jul 2025 22:21:08 GMT
<
{"status":"OK"}
* Closing connection 0
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication#
```

### Task1:
api/v1/app.py
```python
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

if __name__ == "__main__":
    # Load host and port from environment or use default
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))
    app.run(host=host, port=port)
```

api/v1/views/index.py
```python
#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
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
def raise_unauthorized():
    """ Raise 401 Unauthorized error """
    abort(401)
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/unauthorized" -vvv
*   Trying 0.0.0.0:5000...
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/unauthorized HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.81.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
* HTTP 1.0, assume close after body
< HTTP/1.0 404 NOT FOUND
< Content-Type: application/json
< Content-Length: 22
< Access-Control-Allow-Origin: *
< Server: Werkzeug/1.0.1 Python/3.10.12
< Date: Wed, 23 Jul 2025 22:14:52 GMT
<
{"error":"Not found"}
* Closing connection 0
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/unauthorized" -vvv
*   Trying 0.0.0.0:5000...
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/unauthorized HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.81.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
* HTTP 1.0, assume close after body
< HTTP/1.0 401 UNAUTHORIZED
< Content-Type: application/json
< Content-Length: 25
< Access-Control-Allow-Origin: *
< Server: Werkzeug/1.0.1 Python/3.10.12
< Date: Wed, 23 Jul 2025 22:16:52 GMT
<
{"error":"Unauthorized"}
* Closing connection 0
```

### Task2:
api/v1/app.py
```python
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
```

api/v1/views/index.py
```python
#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
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
def raise_unauthorized():
    """ Raise 401 Unauthorized error """
    abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def raise_forbidden():
    """ GET /api/v1/forbidden - Raise a 403 Forbidden error """
    abort(403)
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/Basic_authentication# c                        c
url http://0.0.0.0:5000/api/v1/forbidden
{"error":"Forbidden"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/forbidden"
{"error":"Forbidden"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/forbidden" -vvv
*   Trying 0.0.0.0...
*   Trying 0.0.0.0:5000...
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/forbidden HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.81.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
* HTTP 1.0, assume close after body
< HTTP/1.0 403 FORBIDDEN
< Content-Type: application/json
< Content-Length: 22
< Access-Control-Allow-Origin: *
< Server: Werkzeug/1.0.1 Python/3.10.12
< Date: Wed, 23 Jul 2025 23:17:04 GMT
<
{"error":"Forbidden"}
* Closing connection 0
/mnt/c/Program Files (x86)/php-8.4.1-Win32-vs17-x64/README.md: line 1: div: No such file or directory
/mnt/c/Program Files (x86)/php-8.4.1-Win32-vs17-x64/README.md: line 2: a: No such file or directory
/mnt/c/Program Files (x86)/php-8.4.1-Win32-vs17-x64/README.md: lin: No such file or directory
/mnt/c/Program Files (x86)/php-8.4.1-Win32-vs17-x64/README.md: line 7: /a: No such file or directory
/mnt/c/Program Files (x86)/php-8.4.1-Win32-vs17-x64/README.md: line 8: /div: No such file or directory
/mnt/c/Program Files (x86)/php-8.4.1-Win32-vs17-x64/README.md: line 9: $'\r': command not found
/mnt/c/Program Files (x86)/php-8.4.1-Win32-vs17-x64/README.md: line 11: $'\r': command not found
/mnt/c/Program Files (x86)/php-8.4.1-Win32-vs17-x64/README.md: line 12: PHP: command not found
/mnt/c/Program Files (x86)/php-8.4.1-Win32-vs17-x64/README.md: line 13: web: command not found
/mnt/c/Program Files (x86)/php-8.4.1-Win32-vs17-x64/README.md: line 14: blog: command not found
/mnt/c/Program Files (x86)/php-8.4.1-Win32-vs17-x64/README.md: line 15: syntax error near unexpected token `('
/mnt/c/Program Files (x86)/php-8.4.1-Win32-vs17-x64/README.md: lin' 15: `[PHP License v3.01](LICENSE).
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication#
```

### Task3:
api/v1/auth
```python

```

api/v1/auth/__init__.py
```python

```
main_0.py
```python
#!/usr/bin/env python3
""" Main 0
"""
from api.v1.auth.auth import Auth

a = Auth()

print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
print(a.authorization_header())
print(a.current_user())
```

api/v1/auth/auth.py
```python
#!/usr/bin/env python3
"""
Auth module for handling API authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Template for all authentication systems
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path

        Returns:
            False for now
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns the Authorization header from the request

        Returns:
            None for now
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user (None for now)

        Returns:
            None
        """
        return None
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# API_HOST=0.0.0.0 API_PORT=5000 ./main_0.py
False
None
None
```

### Task4:
api/v1/auth/auth.py
```python
#!/usr/bin/env python3
"""
Auth module for handling API authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Template for all authentication systems
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
        Returns True if path is not in excluded_paths.
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        # Ensure path ends with '/' for comparison
        if not path.endswith('/'):
            path += '/'

        for excluded in excluded_paths:
            if excluded.endswith('*'):
                # Handle wildcard prefix match
                if path.startswith(excluded[:-1]):
                    return False
            elif path == excluded:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the Authorization header from the request

        Returns:
            None for now
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user (None for now)

        Returns:
            None
        """
        return None
```

main_1.py
```python
bob@dylan:~$ cat main_1.py
#!/usr/bin/env python3
""" Main 1
"""
from api.v1.auth.auth import Auth

a = Auth()

print(a.require_auth(None, None))
print(a.require_auth(None, []))
print(a.require_auth("/api/v1/status/", []))
print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/status", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/users", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/users", ["/api/v1/status/", "/api/v1/stats"]))
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/Basic_authentication#
API_HOST=0.0.0.0 API_PORT=5000 ./main_1.py
True
True
True
False
False
True
True
```

### Task5:
api/v1/app.py
```python
#!/usr/bin/env python3
"""
Route module for the API
Sets up the Flask app and registers blueprints, error handlers, and CORS.
"""

from os import getenv
from flask import Flask, jsonify
from flask_cors import CORS
from api.v1.views import app_views
from api.v1.auth.auth import Auth
from flask import abort, request

auth = None
if getenv("AUTH_TYPE") == "auth":
    auth = Auth()


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


@app.before_request
def before_request_func():
    """
    Validates all requests before they reach route handlers
    """
    if auth is None:
        return

    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                      '/api/v1/forbidden/']

    if not auth.require_auth(request.path, excluded_paths):
        return

    if auth.authorization_header(request) is None:
        abort(401)

    if auth.current_user(request) is None:
        abort(403)


if __name__ == "__main__":
    # Load host and port from environment or use default
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))
    app.run(host=host, port=port)
```

api/v1/auth/auth.py
```python
#!/usr/bin/env python3
"""
Auth module for handling API authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Template for all authentication systems
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
        Returns True if path is not in excluded_paths.
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        # Ensure path ends with '/' for comparison
        if not path.endswith('/'):
            path += '/'

        for excluded in excluded_paths:
            if excluded.endswith('*'):
                # Handle wildcard prefix match
                if path.startswith(excluded[:-1]):
                    return False
            elif path == excluded:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the Authorization header from the request
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user (None for now)

        Returns:
            None
        """
        return None
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=auth python3 -m api.v1.app
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.71.179:5000 (Press CTRL+C to quit)
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/status"
{"status":"OK"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/status/"
{"status":"OK"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/users"
{"error":"Unauthorized"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
{"error":"Forbidden"}
```

### Task6:
api/v1/app.py
```python
#!/usr/bin/env python3
"""
Route module for the API
Sets up the Flask app and registers blueprints, error handlers, and CORS.
"""

from os import getenv
from flask import Flask, jsonify
from flask_cors import CORS
from api.v1.views import app_views
from api.v1.auth.auth import Auth
from flask import abort, request

auth = None
auth_type = getenv("AUTH_TYPE")

if auth_type == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()
elif auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()



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


@app.before_request
def before_request_func():
    """
    Validates all requests before they reach route handlers
    """
    if auth is None:
        return

    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                      '/api/v1/forbidden/']

    if not auth.require_auth(request.path, excluded_paths):
        return

    if auth.authorization_header(request) is None:
        abort(401)

    if auth.current_user(request) is None:
        abort(403)


if __name__ == "__main__":
    # Load host and port from environment or use default
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))
    app.run(host=host, port=port)

```

api/v1/auth/basic_auth.py
```python
#!/usr/bin/env python3
"""
BasicAuth module for handling Basic Authentication
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class inherits from Auth
    For now, it does nothing, just a placeholder
    """
    pass
```

api/v1/auth/auth.py
```python
#!/usr/bin/env python3
"""
Auth module for handling API authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Template for all authentication systems
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
        Returns True if path is not in excluded_paths.
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        # Ensure path ends with '/' for comparison
        if not path.endswith('/'):
            path += '/'

        for excluded in excluded_paths:
            if excluded.endswith('*'):
                # Handle wildcard prefix match
                if path.startswith(excluded[:-1]):
                    return False
            elif path == excluded:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the Authorization header from the request
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user (None for now)

        Returns:
            None
        """
        return None
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.71.179:5000 (Press CTRL+C to quit)
127.0.0.1 - - [24/Jul/2025 22:29:39] "GET /api/v1/status HTTP/1.1" 200 -
127.0.0.1 - - [24/Jul/2025 22:29:39] "GET /api/v1/users HTTP/1.1" 401 -
127.0.0.1 - - [24/Jul/2025 22:29:39] "GET /api/v1/users HTTP/1.1" 403 -
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/status"
# Résultat : {"status": "OK"}

curl "http://0.0.0.0:5000/api/v1/users"
# Résultat : {"error": "Unauthorized"}

curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
# Résultat : {"error": "Forbidden"}
{"status":"OK"}
{"error":"Unauthorized"}
{"error":"Forbidden"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication#
```

### Task7:
api/v1/app.py
```python
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

auth = None
auth_type = getenv("AUTH_TYPE")

if auth_type == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()
elif auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()

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


@app.before_request
def before_request_func():
    """
    Validates all requests before they reach route handlers
    """
    if auth is None:
        return

    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                      '/api/v1/forbidden/']

    if not auth.require_auth(request.path, excluded_paths):
        return

    if auth.authorization_header(request) is None:
        abort(401)

    if auth.current_user(request) is None:
        abort(403)


if __name__ == "__main__":
    # Load host and port from environment or use default
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))
    app.run(host=host, port=port)
```

api/v1/auth/basic_auth.py
```python
#!/usr/bin/env python3
"""
BasicAuth module for handling Basic Authentication
"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """
    BasicAuth class inherits from Auth
    For now, it does nothing, just a placeholder
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:

        """
        Extracts the Base64 part of the Authorization header for Basic Auth

        Args:
            authorization_header (str): The "Authorization" header

        Returns:
            str: Base64 part (after "Basic "), or None if invalid
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[len("Basic "):]
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/status"
{"status":"OK"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/status/"
{"status":"OK"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/users"
{"error":"Unauthorized"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
{"error":"Forbidden"}
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.71.179:5000 (Press CTRL+C to quit)
127.0.0.1 - - [24/Jul/2025 22:50:58] "GET /api/v1/status HTTP/1.1" 200 -
127.0.0.1 - - [24/Jul/2025 22:51:07] "GET /api/v1/status/ HTTP/1.1" 200 -
127.0.0.1 - - [24/Jul/2025 22:51:17] "GET /api/v1/users HTTP/1.1" 401 -
127.0.0.1 - - [24/Jul/2025 22:51:26] "GET /api/v1/users HTTP/1.1" 403 -
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# API_HOST=0.0.0.0 API_PORT=5000 ./main_2.py
None
None
None
Holberton
SG9sYmVydG9u
SG9sYmVydG9uIFNjaG9vbA==
None
````

### Task8:
api/v1/auth/basic_auth.py
```python
#!/usr/bin/env python3
"""
BasicAuth module for handling Basic Authentication
"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """
    BasicAuth class inherits from Auth
    For now, it does nothing, just a placeholder
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:

        """
        Extracts the Base64 part of the Authorization header for Basic Auth

        Args:
            authorization_header (str): The "Authorization" header

        Returns:
            str: Base64 part (after "Basic "), or None if invalid
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes a Base64-encoded string to a UTF-8 string

        Args:
            base64_authorization_header (str): Base64 string to decode

        Returns:
            str: Decoded UTF-8 string, or None if invalid or error
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None
```

```bash
bob@dylan:~$ cat main_3.py
#!/usr/bin/env python3
""" Main 3
"""
from api.v1.auth.basic_auth import BasicAuth

a = BasicAuth()

print(a.decode_base64_authorization_header(None))
print(a.decode_base64_authorization_header(89))
print(a.decode_base64_authorization_header("Holberton School"))
print(a.decode_base64_authorization_header("SG9sYmVydG9u"))
print(a.decode_base64_authorization_header("SG9sYmVydG9uIFNjaG9vbA=="))
print(a.decode_base64_authorization_header(a.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA==")))
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# API_HOST=0.0.0.0 API_PORT=5000 ./main_3.py
None
None
None
Holberton
Holberton School
Holberton School
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication#
```

### Task9:
api/v1/auth/basic_auth.py
```python
#!/usr/bin/env python3
"""
BasicAuth module for handling Basic Authentication
"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """
    BasicAuth class inherits from Auth
    For now, it does nothing, just a placeholder
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:

        """
        Extracts the Base64 part of the Authorization header for Basic Auth

        Args:
            authorization_header (str): The "Authorization" header

        Returns:
            str: Base64 part (after "Basic "), or None if invalid
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes a Base64-encoded string to a UTF-8 string

        Args:
            base64_authorization_header (str): Base64 string to decode

        Returns:
            str: Decoded UTF-8 string, or None if invalid or error
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts user credentials from the Base64 decoded string

        Args:
            decoded_base64_authorization_header (str): string in format 'email:password'

        Returns:
            tuple: (email, password) or (None, None) if invalid
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(':', 1))
```

```bash
bob@dylan:~$ cat main_4.py
#!/usr/bin/env python3
""" Main 4
"""
from api.v1.auth.basic_auth import BasicAuth

a = BasicAuth()

print(a.extract_user_credentials(None))
print(a.extract_user_credentials(89))
print(a.extract_user_credentials("Holberton School"))
print(a.extract_user_credentials("Holberton:School"))
print(a.extract_user_credentials("bob@gmail.com:toto1234"))
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# API_HOST=0.0.0.0 API_PORT=5000 ./main_4.py
(None, None)
(None, None)
(None, None)
('Holberton', 'School')
('bob@gmail.com', 'toto1234')
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication#
```

### Task10:
api/v1/auth/basic_auth.py
```python
#!/usr/bin/env python3
"""
BasicAuth module for handling Basic Authentication
"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """
    BasicAuth class inherits from Auth
    For now, it does nothing, just a placeholder
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:

        """
        Extracts the Base64 part of the Authorization header for Basic Auth

        Args:
            authorization_header (str): The "Authorization" header

        Returns:
            str: Base64 part (after "Basic "), or None if invalid
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes a Base64-encoded string to a UTF-8 string

        Args:
            base64_authorization_header (str): Base64 string to decode

        Returns:
            str: Decoded UTF-8 string, or None if invalid or error
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts user credentials from the Base64 decoded string

        Args:
            decoded_base64_authorization_header (str): string in format
                'email:password'

        Returns:
            tuple: (email, password) or (None, None) if invalid
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Retrieves a User instance based on email and password.

        Args:
            user_email (str): user email
            user_pwd (str): user password

        Returns:
            User instance if credentials are valid, else None
        """
        from models.user import User

        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None
        if user_email == "" or user_pwd == "":
            return None

        try:
            users = User.search({"email": user_email})
        except Exception:
            return None

        if not users:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user
```

main_5.py
```bash
#!/usr/bin/env python3
""" Main 5
"""
import uuid
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

""" Create a user test """
user_email = str(uuid.uuid4())
user_clear_pwd = str(uuid.uuid4())
user = User()
user.email = user_email
user.first_name = "Bob"
user.last_name = "Dylan"
user.password = user_clear_pwd
print("New user: {}".format(user.display_name()))
user.save()

""" Retreive this user via the class BasicAuth """

a = BasicAuth()

u = a.user_object_from_credentials(None, None)
print(u.display_name() if u is not None else "None")

u = a.user_object_from_credentials(89, 98)
print(u.display_name() if u is not None else "None")

u = a.user_object_from_credentials("email@notfound.com", "pwd")
print(u.display_name() if u is not None else "None")

u = a.user_object_from_credentials(user_email, "pwd")
print(u.display_name() if u is not None else "None")

u = a.user_object_from_credentials(user_email, user_clear_pwd)
print(u.display_name() if u is not None else "None")
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# API_HOST=0.0.0.0 API_PORT=5000 ./main_5.py
New user: Bob Dylan
None
None
None
None
Bob Dylan
```

### Task11:
api/v1/auth/basic_auth.py
```python

```


main_5.py
```bash
#!/usr/bin/env python3
""" Main 6
"""
import base64
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

""" Create a user test """
user_email = "bob@hbtn.io"
user_clear_pwd = "H0lbertonSchool98!"
user = User()
user.email = user_email
user.password = user_clear_pwd
print("New user: {} / {}".format(user.id, user.display_name()))
user.save()

basic_clear = "{}:{}".format(user_email, user_clear_pwd)
print("Basic Base64: {}".format(base64.b64encode(basic_clear.encode('utf-8')).decode("utf-8")))
```

```bash

```

### Task12:
api/v1/auth/basic_auth.py
```python

```

```bash

```

### Task13:
api/v1/auth/auth.py
```python

```

```bash

```
