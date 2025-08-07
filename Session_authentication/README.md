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
    excluded_paths = ['/api/v1/status/', '/api/v1/status',
                    '/api/v1/unauthorized/', '/api/v1/unauthorized',
                    '/api/v1/forbidden/', '/api/v1/forbidden']


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


main_6.py
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
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-w
eb_back_end/Basic_authentication# API_HOST=0.0.0.0 API_PORT=5000 ./main_6.py
New user: 4ca1f939-bb68-4298-b111-2e234b47eee6 / bob@hbtn.io
Basic Base64: Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-w
eb_back_end/Basic_authentication# API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
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
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/users"
{"error":"Unauthorized"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
{"error":"Forbidden"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic test"
{"error":"Forbidden"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
[{"created_at":"2025-07-25T12:29:39","email":"bob@hbtn.io","first_name":null,"id":"4ca1f939-bb68-4298-b111-2e234b47eee6","last_name":null,"updated_at":"2025-07-25T12:29:39"}]
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication#
```

### Task12:
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

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the User instance for a given request using Basic Auth

        Args:
            request: Flask request object

        Returns:
            User instance if authentication is successful, else None
        """
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_auth = self.extract_base64_authorization_header(auth_header)
        if base64_auth is None:
            return None

        decoded = self.decode_base64_authorization_header(base64_auth)
        if decoded is None:
            return None

        user_email, user_pwd = self.extract_user_credentials(decoded)
        if user_email is None or user_pwd is None:
            return None

        return self.user_object_from_credentials(user_email, user_pwd)
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# API_HOST=0.0.0.0 API_PORT=5000 ./main_100.py
New user: ae2e3c73-a422-48e9-be71-f9f14c0b0d52
Basic Base64: Ym9iMTAwQGhidG4uaW86SDBsYmVydG9uOlNjaG9vbDo5OCE=
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
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/status"
{"status":"OK"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/users"
{"error":"Unauthorized"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
{"error":"Forbidden"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic test"
{"error":"Forbidden"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication# curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iMTAwQGhidG4uaW86SDBsYmVydG9uOlNjaG9vbDo5OCE="
[{"created_at":"2025-07-25T12:34:05","email":"bob100@hbtn.io","first_name":null,"id":"ae2e3c73-a422-48e9-be71-f9f14c0b0d52","last_name":null,"updated_at":"2025-07-25T12:34:05"}]
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Basic_authentication#
```

### Task13:
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

```

```bash

```

# Project Session authentication

### Task0:

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
    excluded_paths = [
        '/api/v1/status/', '/api/v1/status',
        '/api/v1/unauthorized/', '/api/v1/unauthorized',
        '/api/v1/forbidden/', '/api/v1/forbidden'
    ]

    if not auth.require_auth(request.path, excluded_paths):
        return

    if auth.authorization_header(request) is None:
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
```

api/v1/views/users.py
```python
#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def view_all_users() -> str:
    """ GET /api/v1/users
    Return:
      - list of all User objects JSON represented
    """
    all_users = [user.to_json() for user in User.all()]
    return jsonify(all_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
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
```

main_0.py
```bash
#!/usr/bin/env python3
""" Main 0
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
print("New user: {}".format(user.id))
user.save()

basic_clear = "{}:{}".format(user_email, user_clear_pwd)
print("Basic Base64: {}".format(base64.b64encode(basic_clear.encode('utf-8')).decode("utf-8")))
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth ./main_0.py
New user: 88bb3b7a-cf60-4ae0-83bb-ed9235aabde0
Basic Base64: Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.71.179:5000 (Press CTRL+C to quit)
127.0.0.1 - - [30/Jul/2025 00:18:37] "GET /api/v1/status HTTP/1.1" 200 -
127.0.0.1 - - [30/Jul/2025 00:18:44] "GET /api/v1/users HTTP/1.1" 401 -
127.0.0.1 - - [30/Jul/2025 00:18:52] "GET /api/v1/users HTTP/1.1" 200 -
127.0.0.1 - - [30/Jul/2025 00:19:02] "GET /api/v1/users/me HTTP/1.1" 200 -

```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/status"
{"status":"OK"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users"
{"error":"Unauthorized"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
[{"created_at":"2025-07-29T22:18:08","email":"bob@hbtn.io","first_name":null,"id":"88bb3b7a-cf60-4ae0-83bb-ed9235aabde0","last_name":null,"updated_at":"2025-07-29T22:18:08"}]
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
{"created_at":"2025-07-29T22:18:08","email":"bob@hbtn.io","first_name":null,"id":"88bb3b7a-cf60-4ae0-83bb-ed9235aabde0","last_name":null,"updated_at":"2025-07-29T22:18:08"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication#
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# pycodestyle api/v1/app.py
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# pycodestyle api/v1/views/users.py
```

### Task1:

api/v1/auth/session_auth.py
```python
#!/usr/bin/env python3
"""
SessionAuth module
Defines a class SessionAuth that inherits from Auth.
This class will handle session-based authentication.
"""

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    SessionAuth class inherits from Auth.
    Currently empty — will be extended later for session management.
    """
    pass

```

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
elif auth_type == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()

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
    excluded_paths = [
        '/api/v1/status/', '/api/v1/status',
        '/api/v1/unauthorized/', '/api/v1/unauthorized',
        '/api/v1/forbidden/', '/api/v1/forbidden'
    ]

    if not auth.require_auth(request.path, excluded_paths):
        return

    if auth.authorization_header(request) is None:
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

```


```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth python3 -m api.v1.app
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
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/status"
{"status":"OK"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/status/"
{"status":"OK"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users"
{"error":"Unauthorized"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
{"error":"Forbidden"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication#
```
### Task implémentation de flasger:

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
        '/apidocs', '/apidocs/', '/apispec_1.json'  # Swagger UI
    ]

    # ✅ Autoriser Swagger static + spec JSON
    if request.path.startswith('/flasgger_static/'):
        return

    # ✅ Autoriser explicitement la spec JSON Swagger
    if request.path == '/apispec_1.json':
        return

    if not auth.require_auth(request.path, excluded_paths):
        return

    if auth.authorization_header(request) is None:
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
```

api/v1/views/index.py
```python
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
```

```bash
http://localhost:5000/apidocs/
```

```bash
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth python3 -m api.v1.app
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth python3 -m api.v1.app
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.71.179:5000 (Press CTRL+C to quit)
^Croot@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth python3 -m api.v1.app
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.71.179:5000 (Press CTRL+C to quit)
127.0.0.1 - - [30/Jul/2025 13:36:56] "GET /apidocs/ HTTP/1.1" 200 -
127.0.0.1 - - [30/Jul/2025 13:36:56] "GET /flasgger_static/swagger-ui.css HTTP/1.1" 304 -
127.0.0.1 - - [30/Jul/2025 13:36:56] "GET /flasgger_static/swagger-ui-bundle.js HTTP/1.1" 304 -
127.0.0.1 - - [30/Jul/2025 13:36:56] "GET /flasgger_static/swagger-ui-standalone-preset.js HTTP/1.1" 304 -
127.0.0.1 - - [30/Jul/2025 13:36:56] "GET /flasgger_static/lib/jquery.min.js HTTP/1.1" 304 -
127.0.0.1 - - [30/Jul/2025 13:36:57] "GET /apispec_1.json HTTP/1.1" 200 -
127.0.0.1 - - [30/Jul/2025 13:36:57] "GET /flasgger_static/favicon-32x32.png HTTP/1.1" 304 -
127.0.0.1 - - [30/Jul/2025 13:37:09] "GET /api/v1/status HTTP/1.1" 200 -
```
![alt text](image.png)

### Task2:

api/v1/auth/session_auth.py
```python
#!/usr/bin/env python3
"""
SessionAuth module
Defines a class SessionAuth that inherits from Auth.
This class will handle session-based authentication.
"""

from api.v1.auth.auth import Auth
import uuid

class SessionAuth(Auth):
    """
    SessionAuth class inherits from Auth.
    Manages user sessions in memory.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session ID for a given user ID.

        Args:
            user_id (str): The ID of the user to create a session for.

        Returns:
            str: The session ID if created, else None.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
```

main_1.py
```bash
#!/usr/bin/env python3
""" Main 1
"""
from api.v1.auth.session_auth import SessionAuth

sa = SessionAuth()

print("{}: {}".format(type(sa.user_id_by_session_id), sa.user_id_by_session_id))

user_id = None
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = 89
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = "abcde"
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = "fghij"
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = "abcde"
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth ./main_1.py
<class 'dict'>: {}
None => None: {}
89 => None: {}
abcde => 9149616e-d659-4464-b54e-72c67eb6d823: {'9149616e-d659-4464-b54e-72c67eb6d823': 'abcde'}
fghij => 453c7115-62ba-48dd-9d1d-0f8ec0d09a26: {'9149616e-d659-4464-b54e-72c67eb6d823': 'abcde', '453c7115-62ba-48dd-9d1d-0f8ec0d09a26': 'fghij'}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication#
```

### Task3:

api/v1/auth/session_auth.py
```python
#!/usr/bin/env python3
"""
SessionAuth module
Defines a class SessionAuth that inherits from Auth.
This class will handle session-based authentication.
"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    SessionAuth class inherits from Auth.
    Manages user sessions in memory.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session ID for a given user ID.

        Args:
            user_id (str): The ID of the user to create a session for.

        Returns:
            str: The session ID if created, else None.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Retrieves the user ID associated with a given session ID.

        Args:
            session_id (str): The session ID to look up.

        Returns:
            str: The user ID if found, else None.
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

```

main_2.py
```bash
#!/usr/bin/env python3
""" Main 2
"""
from api.v1.auth.session_auth import SessionAuth

sa = SessionAuth()

user_id_1 = "abcde"
session_1 = sa.create_session(user_id_1)
print("{} => {}: {}".format(user_id_1, session_1, sa.user_id_by_session_id))

user_id_2 = "fghij"
session_2 = sa.create_session(user_id_2)
print("{} => {}: {}".format(user_id_2, session_2, sa.user_id_by_session_id))

print("---")

tmp_session_id = None
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print("{} => {}".format(tmp_session_id, tmp_user_id))

tmp_session_id = 89
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print("{} => {}".format(tmp_session_id, tmp_user_id))

tmp_session_id = "doesntexist"
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print("{} => {}".format(tmp_session_id, tmp_user_id))

print("---")

tmp_session_id = session_1
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print("{} => {}".format(tmp_session_id, tmp_user_id))

tmp_session_id = session_2
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print("{} => {}".format(tmp_session_id, tmp_user_id))

print("---")

session_1_bis = sa.create_session(user_id_1)
print("{} => {}: {}".format(user_id_1, session_1_bis, sa.user_id_by_session_id))

tmp_user_id = sa.user_id_for_session_id(session_1_bis)
print("{} => {}".format(session_1_bis, tmp_user_id))

tmp_user_id = sa.user_id_for_session_id(session_1)
print("{} => {}".format(session_1, tmp_user_id))
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth ./main_2.py
abcde => c8c4eb59-5d7a-48ff-a51f-822f59fdaf63: {'c8c4eb59-5d7a-48ff-a51f-822f59fdaf63': 'abcde'}
fghij => 10b7a83e-c61d-4230-b69d-ef6334f7cf58: {'c8c4eb59-5d7a-48ff-a51f-822f59fdaf63': 'abcde', '10b7a83e-c61d-4230-b69d-ef6334f7cf58': 'fghij'}
---
None => None
89 => None
doesntexist => None
---
c8c4eb59-5d7a-48ff-a51f-822f59fdaf63 => abcde
10b7a83e-c61d-4230-b69d-ef6334f7cf58 => fghij
---
abcde => be1cb781-f804-4fe8-adca-a0cc445869d8: {'c8c4eb59-5d7a-48ff-a51f-822f59fdaf63': 'abcde', '10b7a83e-c61d-4230-b69d-ef6334f7cf58': 'fghij', 'be1cb781-f804-4fe8-adca-a0cc445869d8': 'abcde'}
be1cb781-f804-4fe8-adca-a0cc445869d8 => abcde
c8c4eb59-5d7a-48ff-a51f-822f59fdaf63 => abcde
```


```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth python3 -m api.v1.app
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.71.179:5000 (Press CTRL+C to quit)
127.0.0.1 - - [30/Jul/2025 15:31:58] "GET / HTTP/1.1" 401 -
127.0.0.1 - - [30/Jul/2025 15:31:59] "GET /favicon.ico HTTP/1.1" 401 -
127.0.0.1 - - [30/Jul/2025 15:32:01] "GET /apidocs/ HTTP/1.1" 200 -
127.0.0.1 - - [30/Jul/2025 15:32:01] "GET /flasgger_static/swagger-ui.css HTTP/1.1" 304 -
127.0.0.1 - - [30/Jul/2025 15:32:01] "GET /flasgger_static/swagger-ui-bundle.js HTTP/1.1" 304 -
127.0.0.1 - - [30/Jul/2025 15:32:01] "GET /flasgger_static/swagger-ui-standalone-preset.js HTTP/1.1" 304 -
127.0.0.1 - - [30/Jul/2025 15:32:01] "GET /flasgger_static/lib/jquery.min.js HTTP/1.1" 304 -
127.0.0.1 - - [30/Jul/2025 15:32:02] "GET /apispec_1.json HTTP/1.1" 200 -
127.0.0.1 - - [30/Jul/2025 15:32:02] "GET /flasgger_static/favicon-32x32.png HTTP/1.1" 304 -

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
from os import getenv


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

    def session_cookie(self, request=None):
        """
        Returns the value of the session cookie from the request.

        Returns:
            str: value of the session cookie (_my_session_id by default)
        """
        if request is None:
            return None

        session_name = getenv("SESSION_NAME")
        if session_name is None:
            return None

        return request.cookies.get(session_name)
```

main_3.py
```bash
#!/usr/bin/env python3
""" Cookie server
"""
from flask import Flask, request
from api.v1.auth.auth import Auth

auth = Auth()

app = Flask(__name__)

@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    """ Root path
    """
    return "Cookie value: {}\n".format(auth.session_cookie(request))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id ./main_3.py
 * Serving Flask app 'main_3' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.71.179:5000 (Press CTRL+C to quit)
127.0.0.1 - - [30/Jul/2025 15:39:49] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [30/Jul/2025 15:40:02] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [30/Jul/2025 15:40:10] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [30/Jul/2025 15:40:19] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [30/Jul/2025 15:40:27] "GET /apidocs/ HTTP/1.1" 404 -
127.0.0.1 - - [30/Jul/2025 15:40:29] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [30/Jul/2025 15:40:29] "GET /.well-known/appspecific/com.chrome.devtools.json HTTP/1.1" 404 -
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000"
Cookie value: None
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000" --cookie "_my_session_id=Hello"
Cookie value: Hello
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000" --cookie "_my_session_id=C is fun"
Cookie value: C is fun
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000" --cookie "_my_session_id_fake"
Cookie value: None
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication#
```

```bash
http://localhost:5000/apidocs/
http://127.0.0.1:5000/apidocs/
http://localhost:5000/
```

![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)


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
    if (auth.authorization_header(request) is None and
            auth.session_cookie(request) is None):
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

```


```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.71.179:5000 (Press CTRL+C to quit)
127.0.0.1 - - [31/Jul/2025 03:59:53] "GET /apidocs/ HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 03:59:53] "GET /flasgger_static/swagger-ui.css HTTP/1.1" 304 -
127.0.0.1 - - [31/Jul/2025 03:59:54] "GET /flasgger_static/swagger-ui-bundle.js HTTP/1.1" 304 -
127.0.0.1 - - [31/Jul/2025 03:59:54] "GET /flasgger_static/swagger-ui-standalone-preset.js HTTP/1.1" 304 -
127.0.0.1 - - [31/Jul/2025 03:59:54] "GET /flasgger_static/lib/jquery.min.js HTTP/1.1" 304 -
127.0.0.1 - - [31/Jul/2025 03:59:54] "GET /apispec_1.json HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 04:00:03] "GET / HTTP/1.1" 401 -
127.0.0.1 - - [31/Jul/2025 04:00:50] "GET /api/v1/status HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 04:00:59] "GET /api/v1/auth_session/login HTTP/1.1" 404 -
127.0.0.1 - - [31/Jul/2025 04:01:06] "GET /api/v1/users/me HTTP/1.1" 401 -
127.0.0.1 - - [31/Jul/2025 04:01:18] "GET /api/v1/users/me HTTP/1.1" 403 -
127.0.0.1 - - [31/Jul/2025 04:01:35] "GET /api/v1/users/me HTTP/1.1" 403 -

```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/status"
{"status":"OK"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/auth_session/login" # not found but not "blocked" by an authentication system
{"error":"Not found"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication#  curl "http://0.0.0.0:5000/api/v1/users/me"
{"error":"Unauthorized"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication#  curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh" # Won't work because the environment variable AUTH_TYPE is equal to "session_auth"
{"error":"Forbidden"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=5535d4d7-3d77-4d06-8281-495dc3acfe76" # Won't work because no user is linked to this Session ID
{"error":"Forbidden"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication#
```

### Task6:

api/v1/auth/session_auth.py
```python
#!/usr/bin/env python3
"""
SessionAuth module
Defines a class SessionAuth that inherits from Auth.
This class will handle session-based authentication.
"""

from api.v1.auth.auth import Auth
import uuid
from models.user import User  # 👈 à ajouter task6


class SessionAuth(Auth):
    """
    SessionAuth class inherits from Auth.
    Manages user sessions in memory.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session ID for a given user ID.

        Args:
            user_id (str): The ID of the user to create a session for.

        Returns:
            str: The session ID if created, else None.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Retrieves the user ID associated with a given session ID.

        Args:
            session_id (str): The session ID to look up.

        Returns:
            str: The user ID if found, else None.
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Returns the User instance for a given request based on session cookie.

        Args:
            request: The Flask request object containing the session cookie.

        Returns:
            User instance if session is valid and user exists, else None.
        """
        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        return User.get(user_id)

```


```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id ./main_4.py
User with ID: 7431597b-a83f-4704-8188-69846cf957bf has a Session ID: 387d9ab1-4ee2-4111-85be-cde50d66f989
 * Serving Flask app 'main_4' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.71.179:5000 (Press CTRL+C to quit)
127.0.0.1 - - [31/Jul/2025 04:18:27] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 04:18:33] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 04:18:46] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 04:19:36] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 04:19:54] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 04:19:59] "GET /.well-known/appspecific/com.chrome.devtools.json HTTP/1.1" 404 -
127.0.0.1 - - [31/Jul/2025 04:20:06] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 04:20:06] "GET /.well-known/appspecific/com.chrome.devtools.json HTTP/1.1" 404 -

```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/"
No user found
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/" --cookie "_my_session_id=Holberton"
No user found
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/" --cookie "_my_session_id=9d1648aa-da79-4692-8236-5f9d7f9e9485"
No user found
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/" --cookie "_my_session_id=387d9ab1-4ee2-4111-85be-cde50d66f989
> ^C
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/" --cookie "_my_session_id=387d9ab1-4ee2-4111-85be-cde50d66f989"
User found: 7431597b-a83f-4704-8188-69846cf957bf
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication#
```

### Task7:

api/v1/views/session_auth.py
```python
#!/usr/bin/env python3
"""
New route for Session Authentication
Handles POST /api/v1/auth_session/login
"""

from flask import request, jsonify, make_response
from flasgger.utils import swag_from

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
```

api/v1/views/__init__.py
```python
#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.session_auth import *

User.load_from_file()

```


```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.71.179:5000 (Press CTRL+C to quit)
127.0.0.1 - - [31/Jul/2025 04:36:54] "GET /api/v1/auth_session/login HTTP/1.1" 405 -
127.0.0.1 - - [31/Jul/2025 04:37:18] "POST /api/v1/auth_session/login HTTP/1.1" 400 -
127.0.0.1 - - [31/Jul/2025 04:38:50] "POST /api/v1/auth_session/login HTTP/1.1" 400 -
127.0.0.1 - - [31/Jul/2025 04:39:03] "POST /api/v1/auth_session/login HTTP/1.1" 404 -
127.0.0.1 - - [31/Jul/2025 04:39:18] "POST /api/v1/auth_session/login HTTP/1.1" 401 -
127.0.0.1 - - [31/Jul/2025 04:39:29] "POST /api/v1/auth_session/login HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 04:39:52] "POST /api/v1/auth_session/login HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 04:40:32] "GET /api/v1/users/me HTTP/1.1" 403 -
127.0.0.1 - - [31/Jul/2025 04:42:21] "GET / HTTP/1.1" 401 -
127.0.0.1 - - [31/Jul/2025 04:42:22] "GET /.well-known/appspecific/com.chrome.devtools.json HTTP/1.1" 401 -
127.0.0.1 - - [31/Jul/2025 04:42:42] "GET /apidocs/ HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 04:42:42] "GET /flasgger_static/swagger-ui.css HTTP/1.1" 304 -
127.0.0.1 - - [31/Jul/2025 04:42:42] "GET /flasgger_static/swagger-ui-bundle.js HTTP/1.1" 304 -
127.0.0.1 - - [31/Jul/2025 04:42:42] "GET /flasgger_static/swagger-ui-standalone-preset.js HTTP/1.1" 304 -
127.0.0.1 - - [31/Jul/2025 04:42:42] "GET /flasgger_static/lib/jquery.min.js HTTP/1.1" 304 -
127.0.0.1 - - [31/Jul/2025 04:42:43] "GET /apispec_1.json HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 04:42:43] "GET /flasgger_static/favicon-32x32.png HTTP/1.1" 304 -
127.0.0.1 - - [31/Jul/2025 04:43:47] "GET /api/v1/users/me HTTP/1.1" 200 -
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication#  curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XGET
{"error":"Not found"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication#  curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XGET
<!doctype html>
<html lang=en>
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST
{"error":"email missing"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=guillaume@hbtn.io"
{"error":"password missing"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=guillaume@hbtn.io" -d "password=test"
{"error":"no user found for this email"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=test"
{"error":"wrong password"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=fake pwd"
{"created_at":"2025-07-31T02:18:05","email":"bobsession@hbtn.io","first_name":null,"id":"7431597b-a83f-4704-8188-69846cf957bf","last_name":null,"updated_at":"2025-07-31T02:18:05"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=fake pwd" -vvv
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 0.0.0.0:5000...
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> POST /api/v1/auth_session/login HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.81.0
> Accept: */*
> Content-Length: 42
> Content-Type: application/x-www-form-urlencoded
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: Werkzeug/2.1.2 Python/3.10.12
< Date: Thu, 31 Jul 2025 02:39:52 GMT
< Content-Type: application/json
< Content-Length: 180
< Set-Cookie: _my_session_id=1da98e7e-c5ce-4179-aade-913bb17bfcfa; Path=/
< Access-Control-Allow-Origin: *
< Connection: close
<
{"created_at":"2025-07-31T02:18:05","email":"bobsession@hbtn.io","first_name":null,"id":"7431597b-a83f-4704-8188-69846cf957bf","last_name":null,"updated_at":"2025-07-31T02:18:05"}
* Closing connection 0
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=df05b4e1-d117-444c-a0cc-ba0d167889c4"
{"error":"Forbidden"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id="


root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=1da98e7e-c5ce-4179-aade-913bb17bfcfa"
{"created_at":"2025-07-31T02:18:05","email":"bobsession@hbtn.io","first_name":null,"id":"7431597b-a83f-4704-8188-69846cf957bf","last_name":null,"updated_at":"2025-07-31T02:18:05"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication#
```
![alt text](image-4.png)
![alt text](image-5.png)
![alt text](image-6.png)

_my_session_id= 14f7a8bf-7dd0-40a6-bde7-3d0fdb3a526e

### Task8:

api/v1/auth/session_auth.py
```python
#!/usr/bin/env python3
"""
SessionAuth module
Defines a class SessionAuth that inherits from Auth.
This class will handle session-based authentication.
"""

from api.v1.auth.auth import Auth
import uuid
from models.user import User  # 👈 à ajouter task6


class SessionAuth(Auth):
    """
    SessionAuth class inherits from Auth.
    Manages user sessions in memory.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session ID for a given user ID.

        Args:
            user_id (str): The ID of the user to create a session for.

        Returns:
            str: The session ID if created, else None.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Retrieves the user ID associated with a given session ID.

        Args:
            session_id (str): The session ID to look up.

        Returns:
            str: The user ID if found, else None.
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Returns the User instance for a given request based on session cookie.

        Args:
            request: The Flask request object containing the session cookie.

        Returns:
            User instance if session is valid and user exists, else None.
        """
        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        return User.get(user_id)

    def destroy_session(self, request=None) -> bool:
        """
        Deletes the session (logout) based on the request cookie.

        Args:
            request: The Flask request object containing the session cookie.

        Returns:
            True if session was deleted, False otherwise.
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        del self.user_id_by_session_id[session_id]
        return True

```

api/v1/views/session_auth.py
```python
#!/usr/bin/env python3
"""
New route for Session Authentication
Handles POST /api/v1/auth_session/login
"""

from flask import request, jsonify, make_response
from flasgger.utils import swag_from
from flask import abort  # task8
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

```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.71.179:5000 (Press CTRL+C to quit)
127.0.0.1 - - [31/Jul/2025 05:14:02] "POST /api/v1/auth_session/login HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 05:14:48] "GET /api/v1/users/me HTTP/1.1" 403 -
127.0.0.1 - - [31/Jul/2025 05:15:02] "GET /api/v1/users/me HTTP/1.1" 403 -
127.0.0.1 - - [31/Jul/2025 05:16:05] "GET /api/v1/users/me HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 05:16:27] "GET /api/v1/auth_session/logout HTTP/1.1" 403 -
127.0.0.1 - - [31/Jul/2025 05:17:10] "GET /api/v1/auth_session/logout HTTP/1.1" 405 -
127.0.0.1 - - [31/Jul/2025 05:17:43] "DELETE /api/v1/auth_session/logout HTTP/1.1" 403 -
127.0.0.1 - - [31/Jul/2025 05:18:13] "DELETE /api/v1/auth_session/logout HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 05:18:33] "GET /api/v1/users/me HTTP/1.1" 403 -
127.0.0.1 - - [31/Jul/2025 05:18:55] "GET /api/v1/users/me HTTP/1.1" 403 -

```

Set-Cookie: _my_session_id=c8fab1bb-7730-46dc-8251-6252f0cde17

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=fake pwd" -vvv
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 0.0.0.0:5000...
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> POST /api/v1/auth_session/login HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.81.0
> Accept: */*
> Content-Length: 42
> Content-Type: application/x-www-form-urlencoded
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: Werkzeug/2.1.2 Python/3.10.12
< Date: Thu, 31 Jul 2025 03:14:02 GMT
< Content-Type: application/json
< Content-Length: 180
< Set-Cookie: _my_session_id=c8fab1bb-7730-46dc-8251-6252f0cde173; Path=/
< Access-Control-Allow-Origin: *
< Connection: close
<
{"created_at":"2025-07-31T02:18:05","email":"bobsession@hbtn.io","first_name":null,"id":"7431597b-a83f-4704-8188-69846cf957bf","last_name":null,"updated_at":"2025-07-31T02:18:05"}
* Closing connection 0
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721"
{"error":"Forbidden"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=7431597b-a83f-4704-8188-69846cf957bf"
{"error":"Forbidden"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=c8fab1bb-7730-46dc-8251-6252f0cde173"
{"created_at":"2025-07-31T02:18:05","email":"bobsession@hbtn.io","first_name":null,"id":"7431597b-a83f-4704-8188-69846cf957bf","last_name":null,"updated_at":"2025-07-31T02:18:05"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/auth_session/logout" --cookie "_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721"
{"error":"Forbidden"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/auth_session/logout" --cookie "_my_session_id=c8fab1bb-7730-46dc-8251-6252f0cde173"
<!doctype html>
<html lang=en>
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/auth_session/logout" --cookie "_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721" -XDELETE
{"error":"Forbidden"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/auth_session/logout" --cookie "_my_session_id=c8fab1bb-7730-46dc-8251-6252f0cde173" -XDELETE
{}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721"
{"error":"Forbidden"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=c8fab1bb-7730-46dc-8251-6252f0cde173"
{"error":"Forbidden"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication#
```

### Task9:

api/v1/auth/session_exp_auth.py
```python
#!/usr/bin/env python3
"""
SessionExpAuth module
Handles session expiration based on SESSION_DURATION env variable.
"""

from datetime import datetime, timedelta
from os import getenv
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """ Session authentication with expiration time. """

    def __init__(self):
        """ Initialize and read session duration from env """
        try:
            self.session_duration = int(getenv("SESSION_DURATION"))
        except (TypeError, ValueError):
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ Create session and store creation datetime """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        # Replace the string value by a dictionary
        self.user_id_by_session_id[session_id] = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Return user_id if session not expired """
        if session_id is None:
            return None

        session_dict = self.user_id_by_session_id.get(session_id)
        if not session_dict or "user_id" not in session_dict:
            return None

        if self.session_duration <= 0:
            return session_dict["user_id"]

        if "created_at" not in session_dict:
            return None

        created_at = session_dict["created_at"]
        if not isinstance(created_at, datetime):
            return None

        if (created_at + timedelta(seconds=self.session_duration)
                < datetime.now()):
            return None

        return session_dict["user_id"]

```

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
elif auth_type == "session_exp_auth":
    from api.v1.auth.session_exp_auth import SessionExpAuth
    auth = SessionExpAuth()


app = Flask(__name__)

# app.config['SWAGGER'] = {
#     'title': 'Session storage API',
#     'uiversion': 3
# }
app.config['SWAGGER'] = {
    'title': '🗂️ Session Storage API',
    'uiversion': 3,
    'description': (
        'Cette API permet la gestion des sessions utilisateur, '
        'avec prise en charge de l’authentification (Token, Basic, Session) '
        'et des opérations sécurisées sur les ressources utilisateur.\n\n'
        'Fonctionnalités principales :\n'
        '- Authentification par header ou cookie\n'
        '- Accès protégé par token/session\n'
        '- Gestion d’erreurs 401, 403, 404 avec retour JSON\n'
        '- Documentation interactive avec Swagger'
    ),
    'version': '1.0.0',
    'termsOfService': '/terms',
    'contact': {
        'name': 'Stéphane Dinahet',
        'email': 'contact@stephanedinahet.fr',
        'url': 'https://stephanedinahet.fr'
    },
    'license': {
        'name': 'MIT License',
        'url': 'https://opensource.org/licenses/MIT'
    },
    'servers': [
        {
            'url': 'http://localhost:5000/api/v1',
            'description': 'Serveur local (développement)'
        },
        {
            'url': 'https://stephanedinahet.fr/api/v1',
            'description': 'Serveur de production'
        }
    ]
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
    if (auth.authorization_header(request) is None and
            auth.session_cookie(request) is None):
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

```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_exp_auth SESSION_NAME=_my_session_id SESSION_DURATION=60 python3 -m api.v1.app
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.71.179:5000 (Press CTRL+C to quit)
127.0.0.1 - - [31/Jul/2025 16:09:16] "POST /api/v1/auth_session/login HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 16:09:59] "GET /api/v1/users/me HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 16:10:39] "GET /api/v1/users/me HTTP/1.1" 403 -
127.0.0.1 - - [31/Jul/2025 16:10:45] "GET /api/v1/users/me HTTP/1.1" 403 -
127.0.0.1 - - [31/Jul/2025 16:11:16] "POST /api/v1/auth_session/login HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 16:11:43] "GET /api/v1/users/me HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 16:11:46] "GET /api/v1/users/me HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 16:11:50] "GET /api/v1/users/me HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 16:11:53] "GET /api/v1/users/me HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 16:11:59] "GET /api/v1/users/me HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 16:12:04] "GET /api/v1/users/me HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 16:12:08] "GET /api/v1/users/me HTTP/1.1" 200 -
127.0.0.1 - - [31/Jul/2025 16:12:20] "GET /api/v1/users/me HTTP/1.1" 403 -

```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=fake pwd" -vvv
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 0.0.0.0:5000...
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> POST /api/v1/auth_session/login HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.81.0
> Accept: */*
> Content-Length: 42
> Content-Type: application/x-www-form-urlencoded
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: Werkzeug/2.1.2 Python/3.10.12
< Date: Thu, 31 Jul 2025 14:11:16 GMT
< Content-Type: application/json
< Content-Length: 180
< Set-Cookie: _my_session_id=55a79cb3-999b-4c6b-9945-e0a07e393c0d; Path=/
< Access-Control-Allow-Origin: *
< Connection: close
<
{"created_at":"2025-07-31T02:18:05","email":"bobsession@hbtn.io","first_name":null,"id":"7431597b-a83f-4704-8188-69846cf957bf","last_name":null,"updated_at":"2025-07-31T02:18:05"}
* Closing connection 0
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=55a79cb3-999b-4c6b-9945-e0a07e393c0d"
{"created_at":"2025-07-31T02:18:05","email":"bobsession@hbtn.io","first_name":null,"id":"7431597b-a83f-4704-8188-69846cf957bf","last_name":null,"updated_at":"2025-07-31T02:18:05"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=55a79cb3-999b-4c6b-9945-e0a07e393c0d"
{"created_at":"2025-07-31T02:18:05","email":"bobsession@hbtn.io","first_name":null,"id":"7431597b-a83f-4704-8188-69846cf957bf","last_name":null,"updated_at":"2025-07-31T02:18:05"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=55a79cb3-999b-4c6b-9945-e0a07e393c0d"
{"created_at":"2025-07-31T02:18:05","email":"bobsession@hbtn.io","first_name":null,"id":"7431597b-a83f-4704-8188-69846cf957bf","last_name":null,"updated_at":"2025-07-31T02:18:05"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=55a79cb3-999b-4c6b-9945-e0a07e393c0d"
{"created_at":"2025-07-31T02:18:05","email":"bobsession@hbtn.io","first_name":null,"id":"7431597b-a83f-4704-8188-69846cf957bf","last_name":null,"updated_at":"2025-07-31T02:18:05"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=55a79cb3-999b-4c6b-9945-e0a07e393c0d"
{"created_at":"2025-07-31T02:18:05","email":"bobsession@hbtn.io","first_name":null,"id":"7431597b-a83f-4704-8188-69846cf957bf","last_name":null,"updated_at":"2025-07-31T02:18:05"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=55a79cb3-999b-4c6b-9945-e0a07e393c0d"
{"created_at":"2025-07-31T02:18:05","email":"bobsession@hbtn.io","first_name":null,"id":"7431597b-a83f-4704-8188-69846cf957bf","last_name":null,"updated_at":"2025-07-31T02:18:05"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=55a79cb3-999b-4c6b-9945-e0a07e393c0d"
{"created_at":"2025-07-31T02:18:05","email":"bobsession@hbtn.io","first_name":null,"id":"7431597b-a83f-4704-8188-69846cf957bf","last_name":null,"updated_at":"2025-07-31T02:18:05"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=55a79cb3-999b-4c6b-9945-e0a07e393c0d"
{"error":"Forbidden"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication#
```

# Task10


api/v1/auth/session_db_auth.py
```python
#!/usr/bin/env python3
"""
SessionDBAuth module
Stores sessions in the database (file) using UserSession.
"""

from datetime import datetime, timedelta
from models.user_session import UserSession
from models.user import User
from api.v1.auth.session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """Session Authentication stored in DB."""

    def create_session(self, user_id=None):
        """Create session and store it in DB"""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        session = UserSession(user_id=user_id, session_id=session_id)
        session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Return user_id if session not expired and exists in DB"""
        if session_id is None:
            return None

        from models.user_session import UserSession
        sessions = UserSession.search({'session_id': session_id})
        if not sessions:
            return None

        session = sessions[0]
        if self.session_duration <= 0:
            return session.user_id

        if not getattr(session, 'created_at', None):
            return None

        if datetime.now() > (
            session.created_at + timedelta(seconds=self.session_duration)
        ):
            return None

        return session.user_id

    def destroy_session(self, request=None):
        """Destroy session in DB"""
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        from models.user_session import UserSession
        sessions = UserSession.search({'session_id': session_id})
        if not sessions:
            return False

        sessions[0].remove()
        return True

```

api/v1/app.py, models/user_session.py
```python
#!/usr/bin/env python3
"""
Defines the UserSession model.
Stores session ID and associated user ID.
"""

from models.base import Base


class UserSession(Base):
    """UserSession model for storing sessions in DB (file)."""

    def __init__(self, *args: list, **kwargs: dict):
        """Initialize session with user_id and session_id"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')

```

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
elif auth_type == "session_exp_auth":
    from api.v1.auth.session_exp_auth import SessionExpAuth
    auth = SessionExpAuth()
elif auth_type == "session_db_auth":
    from api.v1.auth.session_db_auth import SessionDBAuth
    auth = SessionDBAuth()


app = Flask(__name__)

# app.config['SWAGGER'] = {
#     'title': 'Session storage API',
#     'uiversion': 3
# }
app.config['SWAGGER'] = {
    'title': '🗂️ Session Storage API',
    'uiversion': 3,
    'description': (
        'Cette API permet la gestion des sessions utilisateur, '
        'avec prise en charge de l’authentification (Token, Basic, Session) '
        'et des opérations sécurisées sur les ressources utilisateur.\n\n'
        'Fonctionnalités principales :\n'
        '- Authentification par header ou cookie\n'
        '- Accès protégé par token/session\n'
        '- Gestion d’erreurs 401, 403, 404 avec retour JSON\n'
        '- Documentation interactive avec Swagger'
    ),
    'version': '1.0.0',
    'termsOfService': '/terms',
    'contact': {
        'name': 'Stéphane Dinahet',
        'email': 'contact@stephanedinahet.fr',
        'url': 'https://stephanedinahet.fr'
    },
    'license': {
        'name': 'MIT License',
        'url': 'https://opensource.org/licenses/MIT'
    },
    'servers': [
        {
            'url': 'http://localhost:5000/api/v1',
            'description': 'Serveur local (développement)'
        },
        {
            'url': 'https://stephanedinahet.fr/api/v1',
            'description': 'Serveur de production'
        }
    ]
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
    if (auth.authorization_header(request) is None and
            auth.session_cookie(request) is None):
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

```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_db_auth SESSION_NAME=_my_session_id SESSION_DURATION=60 python3 -m api.v1.app
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
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=fake pwd" -vvv
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 0.0.0.0:5000...
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> POST /api/v1/auth_session/login HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.81.0
> Accept: */*
> Content-Length: 42
> Content-Type: application/x-www-form-urlencoded
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: Werkzeug/2.1.2 Python/3.10.12
< Date: Thu, 31 Jul 2025 14:26:30 GMT
< Content-Type: application/json
< Content-Length: 180
< Set-Cookie: _my_session_id=53798cba-eba3-4975-bddf-43782ce3461c; Path=/
< Access-Control-Allow-Origin: *
< Connection: close
<
{"created_at":"2025-07-31T02:18:05","email":"bobsession@hbtn.io","first_name":null,"id":"7431597b-a83f-4704-8188-69846cf957bf","last_name":null,"updated_at":"2025-07-31T02:18:05"}
* Closing connection 0
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=53798cba-eba3-4975-bddf-43782ce3461c"
{"error":"Forbidden"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsc
hool-web_back_end/Session_authentication#
```






```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication# API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_db_auth SESSION_NAME=_my_session_id SESSION_DURATION=60 python3 -m api.v1.app
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.71.179:5000 (Press CTRL+C to quit)
127.0.0.1 - - [06/Aug/2025 01:00:58] "POST /api/v1/auth_session/login HTTP/1.1" 200 -
>>> session_id reçu: 9c96dd89-13b4-4eda-bcfb-72058c12affd
>>> Sessions trouvées: [<models.user_session.UserSession object at 0x7f33b4a804c0>]
>>> Session chargée: <models.user_session.UserSession object at 0x7f33b4a804c0>
>>> created_at: 2025-08-05 23:00:58.228025
>>> now: 2025-08-06 01:01:42.214711
>>> expire_at: 2025-08-05 23:01:58.228025
>>> session_duration: 60
127.0.0.1 - - [06/Aug/2025 01:01:42] "GET /api/v1/users/me HTTP/1.1" 200 -
>>> session_id reçu: 9c96dd89-13b4-4eda-bcfb-72058c12affd
>>> Sessions trouvées: [<models.user_session.UserSession object at 0x7f33b4a804c0>]
>>> Session chargée: <models.user_session.UserSession object at 0x7f33b4a804c0>
>>> created_at: 2025-08-05 23:00:58.228025
>>> now: 2025-08-06 01:01:59.645215
>>> expire_at: 2025-08-05 23:01:58.228025
>>> session_duration: 60
>>> Session expirée
127.0.0.1 - - [06/Aug/2025 01:01:59] "GET /api/v1/users/me HTTP/1.1" 403 -
>>> session_id reçu: 9c96dd89-13b4-4eda-bcfb-72058c12affd
>>> Sessions trouvées: [<models.user_session.UserSession object at 0x7f33b4a804c0>]
>>> Session chargée: <models.user_session.UserSession object at 0x7f33b4a804c0>
>>> created_at: 2025-08-05 23:00:58.228025
>>> now: 2025-08-06 01:02:03.199187
>>> expire_at: 2025-08-05 23:01:58.228025
>>> session_duration: 60
>>> Session expirée
127.0.0.1 - - [06/Aug/2025 01:02:03] "GET /api/v1/users/me HTTP/1.1" 403 -
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=fake pwd" -vvv
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 0.0.0.0:5000...
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> POST /api/v1/auth_session/login HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.81.0
> Accept: */*
> Content-Length: 42
> Content-Type: application/x-www-form-urlencoded
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: Werkzeug/2.1.2 Python/3.10.12
< Date: Tue, 05 Aug 2025 23:00:58 GMT
< Content-Type: application/json
< Content-Length: 186
< Set-Cookie: _my_session_id=9c96dd89-13b4-4eda-bcfb-72058c12affd; Path=/
< Access-Control-Allow-Origin: *
< Connection: close
<
{"created_at":"2025-08-05T22:56:04","email":"bobsession@hbtn.io","first_name":"Bob","id":"861726af-af4a-4a54-9374-e90c2f63393f","last_name":"Session","updated_at":"2025-08-05T22:56:04"}
* Closing connection 0
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=9c96dd89-13b4-4eda-bcfb-72058c12affd"
{"created_at":"2025-08-05T22:56:04","email":"bobsession@hbtn.io","first_name":"Bob","id":"861726af-af4a-4a54-9374-e90c2f63393f","last_name":"Session","updated_at":"2025-08-05T22:56:04"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=9c96dd89-13b4-4eda-bcfb-72058c12affd"
{"error":"Forbidden"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=9c96dd89-13b4-4eda-bcfb-72058c12affd"
{"error":"Forbidden"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication#
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication# python3 setup_0.py
User created:
861726af-af4a-4a54-9374-e90c2f63393f
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication# python3 test/python_e2e.py

Session ID: c3fb2dae-1abb-443c-a894-69c81fbb8c1f
User me (immédiat) OK
User me (10s) OK
User me (session expirée) OK
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication# python3 test/python_e2e.py

Session ID: 93a7af31-93e1-4142-866d-b4ac27950156
User me (immédiat) OK
User me (10s) OK
Waiting for session to expire (65s)...
User me (session expirée) OK
```


![alt text](image-7.png)

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication# cat .db_UserSession.json | jq .
{
  "986fdf71-59ff-4a30-b462-f203d64e31ab": {
    "user_id": "861726af-af4a-4a54-9374-e90c2f63393f",
    "session_id": "7f0903ac-aa73-48c9-af8e-6536a698061f",
    "id": "986fdf71-59ff-4a30-b462-f203d64e31ab",
    "created_at": "2025-08-06T10:37:16",
    "updated_at": "2025-08-06T10:37:16"
  },
  "22e0417d-44f1-4c79-b421-2108c4174980": {
    "user_id": "861726af-af4a-4a54-9374-e90c2f63393f",
    "session_id": "10f459c7-657f-4b7d-ae8d-1055e2148901",
    "id": "22e0417d-44f1-4c79-b421-2108c4174980",
    "created_at": "2025-08-06T10:37:26",
    "updated_at": "2025-08-06T10:37:26"
  }
}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication#
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication# curl -XPOST "http://0.0.0.0:5000/api/v1/auth_session/login" \
  -d "email=bobsession@hbtn.io" -d "password=fake pwd" -c cookie.txt
{"created_at":"2025-08-05T22:56:04","email":"bobsession@hbtn.io","first_name":"Bob","id":"861726af-af4a-4a54-9374-e90c2f63393f","last_name":"Session","updated_at":"2025-08-05T22:56:04"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" -b cookie.txt
{"created_at":"2025-08-05T22:56:04","email":"bobsession@hbtn.io","first_name":"Bob","id":"861726af-af4a-4a54-9374-e90c2f63393f","last_name":"Session","updated_at":"2025-08-05T22:56:04"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" -b cookie.txt
{"created_at":"2025-08-05T22:56:04","email":"bobsession@hbtn.io","first_name":"Bob","id":"861726af-af4a-4a54-9374-e90c2f63393f","last_name":"Session","updated_at":"2025-08-05T22:56:04"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" -b cookie.txt
{"created_at":"2025-08-05T22:56:04","email":"bobsession@hbtn.io","first_name":"Bob","id":"861726af-af4a-4a54-9374-e90c2f63393f","last_name":"Session","updated_at":"2025-08-05T22:56:04"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication# curl "http://0.0.0.0:5000/api/v1/users/me" -b cookie.txt
{"error":"Forbidden"}
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication#
```

```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication# python3 main_8.py
🔄 Rechargement des utilisateurs...
📦 Création d'une instance SessionDBAuth...
👤 Recherche de l'utilisateur bobsession@hbtn.io...
✅ Utilisateur trouvé : 861726af-af4a-4a54-9374-e90c2f63393f
🔐 Création d'une session pour cet utilisateur...
✅ Session ID : 10dce793-5dc2-47f8-ab0b-cb1dc7956b61
📂 Vérification de la session créée en base...
✅ Session trouvée : user_id = 861726af-af4a-4a54-9374-e90c2f63393f
🔎 Récupération de l'user_id depuis la session...
✅ user_id récupéré : 861726af-af4a-4a54-9374-e90c2f63393f
⏳ Attente 3 secondes (durée de session courte recommandée pour test)...
❌ Suppression de la session...
🗑️ Suppression de l'objet 206f7d92-b193-4828-a222-85ace66a5cd8 danss UserSession
✅ Session supprimée ? True
🔍 Nouvelle tentative de récupération après suppression...
>>> Aucune session trouvée avec cet ID
Résultat attendu : None → Résultat réel : None
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication#

root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication# python3 test/python_e2e.py
Session ID: c58edd70-e675-4aa7-b284-ec8dc072777e
User me (immédiat) OK
User me (10s) OK
Waiting for session to expire (65s)...
User me (session expirée) OK
```


```bash
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication# pycodestyle models/user_session.py api/v1/auth/session_db_auth.py
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication# python3 main_8.py
🔄 Rechargement des utilisateurs...
📦 Création d'une instance SessionDBAuth...
👤 Recherche de l'utilisateur bobsession@hbtn.io...
✅ Utilisateur trouvé : 861726af-af4a-4a54-9374-e90c2f63393f
🔐 Création d'une session pour cet utilisateur...
✅ Session ID : f257e364-6697-453c-97a7-73bbdd7b3c6f
📂 Vérification de la session créée en base...
✅ Session trouvée : user_id = 861726af-af4a-4a54-9374-e90c2f63393f
🔎 Récupération de l'user_id depuis la session...
✅ user_id récupéré : 861726af-af4a-4a54-9374-e90c2f63393f
⏳ Attente 3 secondes (durée de session courte recommandée pour test)...
❌ Suppression de la session...
🗑️ Suppression de l'objet 9849425b-25fc-48bb-b3aa-775b3a3c0830 danss UserSession
✅ Session supprimée ? True
🔍 Nouvelle tentative de récupération après suppression...
Résultat attendu : None → Résultat réel : None
root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonsch
ool-web_back_end/Session_authentication# python3 test/python_e2e.py
Session ID: 5efb80d0-27a4-41d5-ada5-a7c2bb824744
User me (immédiat) OK
User me (10s) OK
Waiting for session to expire (65s)...
User me (session expirée) OK
```
