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
