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
