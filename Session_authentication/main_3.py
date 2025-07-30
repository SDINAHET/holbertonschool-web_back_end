#!/usr/bin/env python3
""" Cookie server
"""
from flask import Flask, request
from api.v1.auth.auth import Auth
from flasgger import Swagger, swag_from


auth = Auth()

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/', methods=['GET'], strict_slashes=False)
@swag_from({
    'tags': ['Cookie'],
    'summary': 'Get the session cookie value',
    'responses': {
        200: {
            'description': 'Returns the value of the session cookie',
            'examples': {
                'application/json': {
                    'cookie': '_my_session_id=XYZ'
                }
            }
        }
    }
})
def root_path():
    """ Root path
    """
    return "Cookie value: {}\n".format(auth.session_cookie(request))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
