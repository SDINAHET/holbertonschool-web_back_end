#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from app import app as flask_app

class TestTask7RegisterUser(unittest.TestCase):
    def setUp(self):
        self.client = flask_app.test_client()

    @patch("app.AUTH")
    def test_register_user_created(self, mock_auth):
        # Simule un enregistrement OK
        mock_auth.register_user.return_value = object()

        resp = self.client.post("/users", data={
            "email": "bob@me.com",
            "password": "mySuperPwd"
        })

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json(), {
            "email": "bob@me.com",
            "message": "user created"
        })
        mock_auth.register_user.assert_called_once_with("bob@me.com", "mySuperPwd")

    @patch("app.AUTH")
    def test_register_user_already_registered(self, mock_auth):
        # Simule l'email déjà pris
        mock_auth.register_user.side_effect = ValueError("email already registered")

        resp = self.client.post("/users", data={
            "email": "bob@me.com",
            "password": "mySuperPwd"
        })

        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.get_json(), {"message": "email already registered"})

if __name__ == "__main__":
    unittest.main(verbosity=2)
