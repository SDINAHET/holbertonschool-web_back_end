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

        if datetime.now() > created_at + timedelta(seconds=self.session_duration):
            return None

        return session_dict["user_id"]
