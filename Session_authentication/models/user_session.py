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
        # super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
        # print("[DEBUG] session stored:", self.__dict__)
        super().__init__(*args, **kwargs)

