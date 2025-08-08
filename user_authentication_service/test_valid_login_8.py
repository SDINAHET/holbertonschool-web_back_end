#!/usr/bin/env python3
import unittest
from unittest.mock import patch, MagicMock
import bcrypt
from sqlalchemy.orm.exc import NoResultFound  # match Auth.valid_login's catch
from auth import Auth


class TestValidLogin(unittest.TestCase):
    """Unit tests for Auth.valid_login (Task 8)"""

    def test_valid_login_correct_credentials(self):
        # Patch DB before creating Auth
        with patch("auth.DB") as mock_db_class, patch("bcrypt.checkpw", return_value=True) as mock_check:
            mock_db = MagicMock()
            mock_db_class.return_value = mock_db

            # Your model stores hashed_password as *str* (since code calls .encode())
            hashed_bytes = bcrypt.hashpw(b"MyPwdOfBob", bcrypt.gensalt())
            hashed_str = hashed_bytes.decode("utf-8")

            user = MagicMock()
            user.hashed_password = hashed_str
            mock_db.find_user_by.return_value = user

            auth = Auth()
            result = auth.valid_login("bob@bob.com", "MyPwdOfBob")

            self.assertTrue(result)
            # bcrypt.checkpw is called with bytes(password) and bytes(hashed_str)
            mock_check.assert_called_once()
            called_args, _ = mock_check.call_args
            self.assertEqual(called_args[0], b"MyPwdOfBob")
            self.assertEqual(called_args[1], hashed_str.encode("utf-8"))

    def test_valid_login_wrong_password(self):
        with patch("auth.DB") as mock_db_class, patch("bcrypt.checkpw", return_value=False):
            mock_db = MagicMock()
            mock_db_class.return_value = mock_db

            hashed_bytes = bcrypt.hashpw(b"MyPwdOfBob", bcrypt.gensalt())
            hashed_str = hashed_bytes.decode("utf-8")

            user = MagicMock()
            user.hashed_password = hashed_str
            mock_db.find_user_by.return_value = user

            auth = Auth()
            result = auth.valid_login("bob@bob.com", "WrongPwd")
            self.assertFalse(result)

    def test_valid_login_unknown_email(self):
        with patch("auth.DB") as mock_db_class:
            mock_db = MagicMock()
            mock_db_class.return_value = mock_db

            # Raise the exact exception your code expects
            mock_db.find_user_by.side_effect = NoResultFound()

            auth = Auth()
            result = auth.valid_login("unknown@email", "MyPwdOfBob")
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
