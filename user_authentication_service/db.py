#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound  # ✅ CORRECT
from sqlalchemy.exc import InvalidRequestError  # ✅ Déjà utilisé


from user import Base, User  # 👈 N'oublie pas d'importer User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database and return the User object."""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find the first user matching the given filters.

        Args:
            **kwargs: fields to filter by.

        Returns:
            User: the user found.

        Raises:
            NoResultFound: if no user matches.
            InvalidRequestError: if an invalid field is provided.
        """
        if not kwargs:
            raise InvalidRequestError

        try:
            user = self._session.query(User).filter_by(**kwargs).first()
        except Exception as e:
            raise InvalidRequestError from e

        if user is None:
            raise NoResultFound

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Met à jour un utilisateur puis commit.
        Lève ValueError si un champ est invalide.
        """
        # récupère l'utilisateur (lèvera NoResultFound si introuvable)
        user = self.find_user_by(id=user_id)

        # applique les mises à jour demandées
        for field, value in kwargs.items():
            if not hasattr(user, field):
                raise ValueError(f"Invalid field: {field}")
            setattr(user, field, value)

        # enregistre en base
        self._session.commit()
