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
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
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
