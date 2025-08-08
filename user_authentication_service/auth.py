#!/usr/bin/env python3
"""Auth module: enregistrement et gestion des utilisateurs."""
from typing import Optional
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4  # ✅ Ajout de l'import pour Task 16

import uuid  # ✅ Ajout de l'import pour Task 9

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Retourne un hash bcrypt (bytes) du mot de passe fourni."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Génère et retourne un UUID4 en chaîne de caractères."""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self) -> None:
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Crée un nouvel utilisateur si l'email n'existe pas.

        - Si l'utilisateur existe déjà: lève ValueError("User <email> already
        exists")
        - Sinon: hash le mot de passe, crée l'utilisateur et le retourne.
        """
        try:
            # S'il existe déjà, find_user_by ne lèvera pas d'exception
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed = _hash_password(password)
            # On enregistre en base sous forme de str (bcrypt renvoie des bytes
            return self._db.add_user(email, hashed.decode("utf-8"))

        # Si on arrive ici, un user existe déjà
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """Valide les identifiants d'un utilisateur."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        if user.hashed_password is None:
            return False

        # bcrypt.checkpw attend les deux valeurs en bytes
        return bcrypt.checkpw(
            password.encode('utf-8'),
            user.hashed_password.encode('utf-8')
        )

    def create_session(self, email: str) -> Optional[str]:
        """Create a session for the user and return the session_id.
        Returns None if the email is unknown.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(
            self, session_id: Optional[str]) -> Optional[User]:
        """
        Récupère un utilisateur à partir de son session_id.

        Args:
            session_id (Optional[str]): ID de session de l'utilisateur

        Returns:
            Optional[User]: L'utilisateur correspondant ou None
        """
        if session_id is None:
            return None

        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Destroys the session for the given user ID by setting
        their session_id to None.
        Uses only public methods of self._db.

        Args:
            user_id (int): ID of the user whose session must be destroyed.

        Returns:
            None
        """
        if user_id is None:
            return None

        try:
            # Récupérer l'utilisateur avec l'ID donné
            user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None

        # Mettre à jour le champ session_id à None
        self._db.update_user(user_id, session_id=None)

        return None

    def get_reset_password_token(self, email: str) -> str:
        """
        Generate a password reset token for the user identified by email.

        - If user doesn't exist -> raise ValueError
        - Otherwise: generate UUID, store it in reset_token, and return it
        """
        if email is None:
            raise ValueError("email is required")

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError("user not found")

        token = str(uuid4())
        self._db.update_user(user.id, reset_token=token)
        return token
