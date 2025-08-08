#!/usr/bin/env python3
import unittest
from unittest.mock import patch, MagicMock
from sqlalchemy.orm.exc import NoResultFound
from auth import Auth


class TestCreateSession(unittest.TestCase):
    """Unit tests for Auth.create_session (Task 10)"""

    def test_create_session_success(self):
        fixed_uuid = "5a006849-343e-4a48-ba4e-bbd523fcca58"

        with patch("auth.DB") as mock_db_class, \
             patch("auth._generate_uuid", return_value=fixed_uuid) as mock_gen_uuid:

            mock_db = MagicMock()
            mock_db_class.return_value = mock_db

            # Fake user found by email
            user = MagicMock()
            user.id = 123
            user.email = "bob@bob.com"
            mock_db.find_user_by.return_value = user

            auth = Auth()
            session_id = auth.create_session("bob@bob.com")

            self.assertEqual(session_id, fixed_uuid)
            mock_gen_uuid.assert_called_once()
            mock_db.find_user_by.assert_called_once_with(email="bob@bob.com")
            mock_db.update_user.assert_called_once_with(user.id, session_id=fixed_uuid)

    def test_create_session_unknown_email(self):
        with patch("auth.DB") as mock_db_class:
            mock_db = MagicMock()
            mock_db_class.return_value = mock_db

            # Simule "user not found" comme le fait la DB
            mock_db.find_user_by.side_effect = NoResultFound()

            auth = Auth()
            session_id = auth.create_session("unknown@email.com")

            self.assertIsNone(session_id)
            mock_db.find_user_by.assert_called_once_with(email="unknown@email.com")
            mock_db.update_user.assert_not_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)
