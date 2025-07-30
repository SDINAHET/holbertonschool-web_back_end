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
