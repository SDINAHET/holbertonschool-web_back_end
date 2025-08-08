import unittest
from auth import Auth

class TestDestroySession(unittest.TestCase):
    def setUp(self):
        self.auth = Auth()
        self.email = "alice@example.com"
        self.password = "s3cret"
        try:
            self.auth.register_user(self.email, self.password)
        except ValueError:
            pass

    def test_destroy_session(self):
        # login & create session
        self.assertTrue(self.auth.valid_login(self.email, self.password))
        sid = self.auth.create_session(self.email)
        self.assertIsNotNone(sid)
        # resolves to a user
        user = self.auth.get_user_from_session_id(sid)
        self.assertIsNotNone(user)
        # destroy by user.id
        self.auth.destroy_session(user.id)
        # old session no longer valid
        self.assertIsNone(self.auth.get_user_from_session_id(sid))

    def test_destroy_session_none(self):
        # should be no-op and not raise
        self.assertIsNone(self.auth.destroy_session(None))

if __name__ == "__main__":
    unittest.main()
