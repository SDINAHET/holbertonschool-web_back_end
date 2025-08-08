#!/usr/bin/env python3
import unittest
from unittest.mock import patch, MagicMock
from sqlalchemy.orm.exc import NoResultFound
from auth import Auth


class TestGetUserFromSessionId(unittest.TestCase):
    """Unit tests for Auth.get_user_from_session_id (Task 12)"""

    def test_returns_user_when_session_exists(self):
        with patch("auth.DB") as mock_db_class:
            mock_db = MagicMock()
            mock_db_class.return_value = mock_db

            user = MagicMock()
            user.id = 1
            user.email = "bob@bob.com"
            mock_db.find_user_by.return_value = user

            auth = Auth()
            out = auth.get_user_from_session_id("163fe508-19a2-48ed-a7c8-d9c6e56fabd1")

            self.assertIs(out, user)
            mock_db.find_user_by.assert_called_once_with(
                session_id="163fe508-19a2-48ed-a7c8-d9c6e56fabd1"
            )

    def test_none_session_id_returns_none_and_skips_db(self):
        with patch("auth.DB") as mock_db_class:
            mock_db = MagicMock()
            mock_db_class.return_value = mock_db

            auth = Auth()
            out = auth.get_user_from_session_id(None)

            self.assertIsNone(out)
            mock_db.find_user_by.assert_not_called()

    def test_unknown_session_id_returns_none(self):
        with patch("auth.DB") as mock_db_class:
            mock_db = MagicMock()
            mock_db_class.return_value = mock_db
            mock_db.find_user_by.side_effect = NoResultFound()

            auth = Auth()
            out = auth.get_user_from_session_id("deadbeef-dead-beef-dead-beefdeadbeef")

            self.assertIsNone(out)
            mock_db.find_user_by.assert_called_once_with(
                session_id="deadbeef-dead-beef-dead-beefdeadbeef"
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
