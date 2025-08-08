import unittest
import importlib
import sys

# if __name__ == "__main__":
#     loader = unittest.TestLoader()
#     suite = unittest.TestSuite()

    # Ajout des tests dans l'ordre souhaité
    # for test_file in [
    #     "test_app_logout_14",
    #     "test_auth_destroy_session_13",
    #     "test_app_profile_15",
    #     "test_auth_reset_token_16",
    #     "test_app_reset_password_token_17",
    #     "test_auth_update_password_18",
    #     "test_app_update_password_19",
    # ]:
    #     suite.addTests(loader.loadTestsFromName(test_file))

    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

ORDERED_TEST_MODULES = [
    # 7 → 19, dans l’ordre
    "test_users_7",
    "test_valid_login_8",
    "test_generate_uuid_9",
    "test_auth_create_session_10",
    "test_app_login_11",
    "test_auth_get_user_from_session_id_12",
    "test_auth_destroy_session_13",
    "test_app_logout_14",
    "test_app_profile_15",
    "test_auth_reset_token_16",
    "test_app_reset_password_token_17",
    "test_auth_update_password_18",
    "test_app_update_password_19",
]

def load_module_safely(name: str):
    try:
        return importlib.import_module(name)
    except Exception as e:
        print(f"[WARN] Impossible d'importer {name}: {e}")
        return None

def main():
    loader = unittest.defaultTestLoader
    suite = unittest.TestSuite()

    for mod_name in ORDERED_TEST_MODULES:
        mod = load_module_safely(mod_name)
        if mod is None:
            continue
        suite.addTests(loader.loadTestsFromModule(mod))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    # Code de sortie non-zéro si échecs/erreurs
    sys.exit(0 if result.wasSuccessful() else 1)

if __name__ == "__main__":
    main()
