import unittest
from app import app, AUTH

class TestUpdatePasswordEndpoint(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.email = "unit19@example.com"
        self.old_pwd = "oldpwd"
        self.new_pwd = "newpwd"
        try:
            AUTH.register_user(self.email, self.old_pwd)
        except ValueError:
            pass

    def test_put_reset_password_missing_fields(self):
        # Manque tout -> 403
        resp = self.client.put("/reset_password", data={})
        self.assertEqual(resp.status_code, 403)

        # Manque un champ -> 403
        resp = self.client.put("/reset_password", data={
            "email": self.email,
            "reset_token": "anything"
        })
        self.assertEqual(resp.status_code, 403)

        resp = self.client.put("/reset_password", data={
            "email": self.email,
            "new_password": self.new_pwd
        })
        self.assertEqual(resp.status_code, 403)

    def test_put_reset_password_invalid_token(self):
        resp = self.client.put("/reset_password", data={
            "email": self.email,
            "reset_token": "not-a-real-token",
            "new_password": self.new_pwd
        })
        self.assertEqual(resp.status_code, 403)

    def test_put_reset_password_success_and_invalidate_token(self):
        # Obtenir un token via POST /reset_password
        r = self.client.post("/reset_password", data={"email": self.email})
        self.assertEqual(r.status_code, 200)
        token = r.get_json().get("reset_token")
        self.assertTrue(token)

        # Mettre à jour le password avec PUT /reset_password
        resp = self.client.put("/reset_password", data={
            "email": self.email,
            "reset_token": token,
            "new_password": self.new_pwd
        })
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json(), {
            "email": self.email,
            "message": "Password updated"
        })

        # Vérifier le changement de mot de passe
        self.assertFalse(AUTH.valid_login(self.email, self.old_pwd))
        self.assertTrue(AUTH.valid_login(self.email, self.new_pwd))

        # Token ne doit plus être réutilisable
        resp = self.client.put("/reset_password", data={
            "email": self.email,
            "reset_token": token,
            "new_password": "anotherpwd"
        })
        self.assertEqual(resp.status_code, 403)

if __name__ == "__main__":
    unittest.main()
