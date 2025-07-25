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
