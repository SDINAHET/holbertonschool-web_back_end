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
