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
