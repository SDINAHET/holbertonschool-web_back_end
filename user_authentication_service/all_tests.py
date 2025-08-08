import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Ajout des tests dans l'ordre souhaité
    for test_file in [
        "test_app_logout_14",
        "test_auth_destroy_session_13",
        "test_app_profile_15",
        "test_auth_reset_token_16",
        "test_app_reset_password_token_17",
        "test_auth_update_password_18",
        "test_app_update_password_19",
    ]:
        suite.addTests(loader.loadTestsFromName(test_file))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
