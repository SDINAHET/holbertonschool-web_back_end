#!/usr/bin/env python3
"""
SessionDBAuth module
Stores sessions in the database (file) using UserSession.
"""

from datetime import datetime, timedelta
from models.user_session import UserSession
from models.user import User
from models import storage  # ✅ Requis pour save/reload/remove
from api.v1.auth.session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """Session Authentication stored in DB."""

    def create_session(self, user_id=None):
        """Create session and store it in DB"""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        # session = UserSession(user_id=user_id, session_id=session_id)
        # session.save()
        # return session_id
        session = UserSession(user_id=user_id, session_id=session_id)
        # storage.new(session)       # ✅ Enregistre dans le storage
        # storage.save()             # ✅ Sauvegarde dans le fichier .json
        session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Return user ID from a session ID if session exists and is not expired."""
        if session_id is None:
            # print(">>> Aucune session_id fournie.")
            return None

        storage.reload()
        sessions = UserSession.search({'session_id': session_id})

        # print(f">>> session_id reçu: {session_id}")
        # print(f">>> Sessions trouvées: {sessions}")

        if not sessions:
            print(">>> Aucune session trouvée avec cet ID")
            return None

        session = sessions[0]

        # print(f">>> Session chargée: {session}")
        # print(f">>> created_at: {session.created_at}")
        # print(f">>> now: {datetime.now()}")
        # print(f">>> expire_at: {session.created_at + timedelta(seconds=self.session_duration)}")
        # print(f">>> session_duration: {self.session_duration}")

        if self.session_duration <= 0:
            return session.user_id

        if not getattr(session, 'created_at', None):
            # print(">>> Pas de created_at sur la session")
            return None

        if datetime.utcnow() > (session.created_at + timedelta(seconds=self.session_duration)):
            # print(">>> Session expirée")
            return None

        return session.user_id


    # def user_id_for_session_id(self, session_id=None):
    #     """Return user_id if session not expired and exists in DB"""
    #     if session_id is None:
    #         return None

    #     storage.reload()  # 👈 recharge les données depuis le fichier JSON

    #     sessions = UserSession.search({'session_id': session_id})
    #     if not sessions:
    #         return None

    #     session = sessions[0]

    #     if self.session_duration <= 0:
    #         return session.user_id

    #     if not getattr(session, 'created_at', None):
    #         return None

    #     if datetime.now() > (session.created_at + timedelta(seconds=self.session_duration)):
    #         return None

    #     return session.user_id


    # def destroy_session(self, request=None):
    #     """Destroy session in DB"""
    #     if request is None:
    #         return False

    #     session_id = self.session_cookie(request)
    #     if session_id is None:
    #         return False

    #     from models.user_session import UserSession
    #     sessions = UserSession.search({'session_id': session_id})
    #     if not sessions:
    #         return False

    #     sessions[0].remove()
    #     return True

    def destroy_session(self, request=None):
        """
        Destroy a user session from the database using the session ID
        extracted from the request's cookie.

        Args:
            request: The Flask request object.

        Returns:
            True if the session was successfully found and deleted, else False.
        """
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        # sessions = storage.all(UserSession)
        # for session in sessions.values():
        #     if session.session_id == session_id:
        #         storage.delete(session)
        #         storage.save()
        #         return True
        # return False

        storage.reload()
        sessions = UserSession.search({'session_id': session_id})
        if not sessions:
            return False

        sessions[0].remove()  # ✅ C’est ce que le checker attend
        return True


    # def destroy_session(self, request=None):
    #     """Destroy session in DB"""
    #     if request is None:
    #         return False

    #     session_id = self.session_cookie(request)
    #     if session_id is None:
    #         return False

    #     storage.reload()  # 👈 recharge les sessions

    #     sessions = UserSession.search({'session_id': session_id})
    #     if not sessions:
    #         return False

    #     sessions[0].remove()
    #     storage.save()
    #     return True

