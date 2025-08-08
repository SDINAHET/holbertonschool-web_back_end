#!/usr/bin/env python3
import unittest
from unittest.mock import patch, MagicMock
from app import app as flask_app


class TestLoginEndpoint(unittest.TestCase):
    def setUp(self):
        self.client = flask_app.test_client()

    @patch("app.AUTH")
    def test_login_success_sets_cookie_and_returns_json(self, mock_auth):
        # Arrange
        mock_auth.valid_login.return_value = True
        mock_auth.create_session.return_value = "163fe508-19a2-48ed-a7c8-d9c6e56fabd1"

        # Act
        resp = self.client.post("/sessions", data={
            "email": "bob@bob.com",
            "password": "mySuperPwd"
        })

        # Assert
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json(), {
            "email": "bob@bob.com",
            "message": "logged in"
        })

        # Cookie header should be present and include the session_id + Path=/
        set_cookie = resp.headers.get("Set-Cookie", "")
        self.assertIn("session_id=163fe508-19a2-48ed-a7c8-d9c6e56fabd1", set_cookie)
        self.assertIn("Path=/", set_cookie)

        mock_auth.valid_login.assert_called_once_with("bob@bob.com", "mySuperPwd")
        mock_auth.create_session.assert_called_once_with("bob@bob.com")

    @patch("app.AUTH")
    def test_login_failure_returns_401(self, mock_auth):
        # Arrange: invalid login -> abort(401)
        mock_auth.valid_login.return_value = False

        # Act
        resp = self.client.post("/sessions", data={
            "email": "bob@bob.com",
            "password": "WrongPwd"
        })

        # Assert
        self.assertEqual(resp.status_code, 401)
        # No session cookie should be set
        self.assertIsNone(resp.headers.get("Set-Cookie"))

        mock_auth.valid_login.assert_called_once_with("bob@bob.com", "WrongPwd")
        mock_auth.create_session.assert_not_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)
