Unittests_and_integration_tests

```bash
$ python -m unittest path/to/test_file.py

python3 -m unittest test_utils.py
python3 -m unittest test_client.py

python3 -m venv .venv
source .venv/bin/activate
deactivate
pip install parameterized
pip install requests
pip freeze > requirements.txt

```

# Task0 test_utils.py

test_utils.py
```python
#!/usr/bin/env python3
"""Unit tests for utils.access_nested_map"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """TestCase for the access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns expected result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()

```

```bash
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests# python3 -m unittest test_utils.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests#
```


# Task1 test_utils.py

test_utils.py
```python
#!/usr/bin/env python3
"""Unit tests for utils.access_nested_map"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """TestCase for the access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns expected result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
    ({}, ("a",)),
    ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised with correct message"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), repr(cm.exception.args[0]))


if __name__ == "__main__":
    unittest.main()

```

```bash
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests# python3 -m unittest test_utils.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests#
```


# Task2 test_utils.py

test_utils.py
```python
#!/usr/bin/env python3
"""Unit tests for utils.access_nested_map"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock



class TestAccessNestedMap(unittest.TestCase):
    """TestCase for the access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns expected result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
    ({}, ("a",)),
    ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised with correct message"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), repr(cm.exception.args[0]))


class TestGetJson(unittest.TestCase):
    """TestCase for the get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json returns payload from mocked requests.get"""
        with patch("utils.requests.get") as mock_get:
            mock_resp = Mock()
            mock_resp.json.return_value = test_payload
            mock_get.return_value = mock_resp

            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()

```

```bash
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests# python3 -m unittest test_utils.py
.....EE
======================================================================
ERROR: test_get_json_0_http_example_com (test_utils.TestGetJson)
Test get_json returns payload from mocked requests.get [with test_url='http://example.com', test_payload={'payload': True}]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/Unittests_and_integration_tests/.venv/lib/python3.10/site-packages/parameterized/parameterized.py", line 620, in standalone_func
    return func(*(a + p.args), **p.kwargs, **kw)
  File "/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/Unittests_and_integration_tests/test_utils.py", line 48, in test_get_json
    self.assertEqual(get_json(test_url), test_payload)
NameError: name 'get_json' is not defined

======================================================================
ERROR: test_get_json_1_http_holberton_io (test_utils.TestGetJson)
Test get_json returns payload from mocked requests.get [with test_url='http://holberton.io', test_payload={'payload': False}]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/Unittests_and_integration_tests/.venv/lib/python3.10/site-packages/parameterized/parameterized.py", line 620, in standalone_func
    return func(*(a + p.args), **p.kwargs, **kw)
  File "/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/Unittests_and_integration_tests/test_utils.py", line 48, in test_get_json
    self.assertEqual(get_json(test_url), test_payload)
NameError: name 'get_json' is not defined

----------------------------------------------------------------------
Ran 7 tests in 0.013s

FAILED (errors=2)
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests# python3 -m unittest test_utils.py
.......
----------------------------------------------------------------------
Ran 7 tests in 0.002s

OK
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests#
```


# Task3 test_utils.py

test_utils.py
```python
#!/usr/bin/env python3
"""Unit tests for utils.access_nested_map"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """TestCase for the access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns expected result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised with correct message"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), repr(cm.exception.args[0]))


class TestGetJson(unittest.TestCase):
    """TestCase for the get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json returns payload from mocked requests.get"""
        with patch("utils.requests.get") as mock_get:
            mock_resp = Mock()
            mock_resp.json.return_value = test_payload
            mock_get.return_value = mock_resp

            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator"""

    def test_memoize(self):
        """a_method is called once even if a_property is accessed twice"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
                TestClass, "a_method", return_value=42) as mock_method:
            obj = TestClass()
            self.assertEqual(obj.a_property, 42)
            self.assertEqual(obj.a_property, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()


```

```bash
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests# python3 -m unittest test_utils.py
.......E
======================================================================
ERROR: test_memoize (test_utils.TestMemoize)
a_method is called once even if a_property is accessed twice
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/Unittests_and_integration_tests/test_utils.py", line 57, in test_memoize
    class TestClass:
  File "/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/Unittests_and_integration_tests/test_utils.py", line 61, in TestClass
    @memoize
NameError: name 'memoize' is not defined

----------------------------------------------------------------------
Ran 8 tests in 0.012s

FAILED (errors=1)
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests# python3 -m unittest test_utils.py
........
----------------------------------------------------------------------
Ran 8 tests in 0.003s

OK
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests#
```


1. Paramétrisation des tests d’exception
💡 Idée : au lieu d’écrire plusieurs tests séparés pour vérifier qu’une fonction lève bien une erreur, on écrit un seul test qui est exécuté avec plusieurs jeux de données.

2. Mock des appels HTTP
💡 Idée : remplacer un vrai appel à un serveur externe par un faux objet (Mock) qui retourne une réponse prédéfinie.
Ça évite :
- de dépendre d’Internet
- d’appeler un vrai serveur pendant les tests
- d’avoir des tests lents ou instables

3. Test de la mémoïsation
💡 Idée : tester qu’une méthode décorée avec @memoize n’est calculée qu’une seule fois, même si on l’appelle plusieurs fois.





# Task4 test_client.py
python3 -m unittest test_client.py

test_client.py
```python
#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient.org"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient.org"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """org should return the JSON payload and call get_json once"""
        expected = {"org": org_name, "repos_url": f"https://api.github.com/orgs/{org_name}/repos"}
        mock_get_json.return_value = expected

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )


if __name__ == "__main__":
    unittest.main()

```

```bash
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests# python3 -m unittest test_client.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests#
```


# Task5 test_client.py

test_client.py
```python
#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient.org"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient.org"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """org should return the JSON payload and call get_json once"""
        expected = {"org": org_name, "repos_url": f"https://api.github.com/orgs/{org_name}/repos"}
        mock_get_json.return_value = expected

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )


class TestGithubOrgClient(unittest.TestCase):
    # tes autres tests (test_org) ...

    def test_public_repos_url(self):
        """_public_repos_url doit renvoyer repos_url depuis org (mockée)"""
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        with patch.object(GithubOrgClient, "org", new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, payload["repos_url"])
            mock_org.assert_called_once()


if __name__ == "__main__":
    unittest.main()
```

```bash
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests# python3 -m unittest test_client.py
E
======================================================================
ERROR: test_public_repos_url (test_client.TestGithubOrgClient)
_public_repos_url doit renvoyer repos_url depuis org (mockée)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back_end/Unittests_and_integration_tests/test_client.py", line 37, in test_public_repos_url
    with patch.object(GithubOrgClient, "org", new_callable=PropertyMock) as mock_org:
NameError: name 'PropertyMock' is not defined

----------------------------------------------------------------------
Ran 1 test in 0.002s

FAILED (errors=1)
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests# python3 -m unittest test_client.py
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests#
```


# Task6 test_client.py

test_client.py
```python
#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient.

This module contains unit tests that validate how GithubOrgClient fetches
organization data and exposes public repositories via its helper methods.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient.org"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """org should return the JSON payload and call get_json once"""
        expected = {
            "org": org_name,
            "repos_url": f"https://api.github.com/orgs/{org_name}/repos"
            }
        mock_get_json.return_value = expected

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """_public_repos_url doit renvoyer repos_url depuis org (mockée)"""
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        with patch.object(
                GithubOrgClient, "org", new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, payload["repos_url"])
            mock_org.assert_called_once()

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """public_repos doit retourner la liste des noms depuis le payload
        mocké"""
        # 1) Mock du payload renvoyé par get_json
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]

        # 2) Mock de la propriété _public_repos_url
        with patch.object(
                GithubOrgClient,
                "_public_repos_url",
                new_callable=PropertyMock
                ) as mock_url:
            mock_url.return_value = "http://example.com/org/repos"

            client = GithubOrgClient("anyorg")
            self.assertEqual(
                    client.public_repos(), ["repo1", "repo2", "repo3"])

            # 3) Vérifications des appels
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                    "http://example.com/org/repos")


if __name__ == "__main__":
    unittest.main()

```

```bash
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests# pycodestyle test_client.py
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests# python3 -m unittest test_client.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests#
```

# Task7 test_client.py

test_client.py
```python
#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient.

This module contains unit tests that validate how GithubOrgClient fetches
organization data and exposes public repositories via its helper methods.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient.org"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """org should return the JSON payload and call get_json once"""
        expected = {
            "org": org_name,
            "repos_url": f"https://api.github.com/orgs/{org_name}/repos"
            }
        mock_get_json.return_value = expected

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """_public_repos_url doit renvoyer repos_url depuis org (mockée)"""
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        with patch.object(
                GithubOrgClient, "org", new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, payload["repos_url"])
            mock_org.assert_called_once()

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """public_repos doit retourner la liste des noms depuis le payload
        mocké"""
        # 1) Mock du payload renvoyé par get_json
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]

        # 2) Mock de la propriété _public_repos_url
        with patch.object(
                GithubOrgClient,
                "_public_repos_url",
                new_callable=PropertyMock
                ) as mock_url:
            mock_url.return_value = "http://example.com/org/repos"

            client = GithubOrgClient("anyorg")
            self.assertEqual(
                    client.public_repos(), ["repo1", "repo2", "repo3"])

            # 3) Vérifications des appels
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                    "http://example.com/org/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Verify that has_license returns the correct boolean."""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected
        )


if __name__ == "__main__":
    unittest.main()

```

```bash
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests# pycodestyle test_client.py
test_client.py:88:1: E303 too many blank lines (3)
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests# pycodestyle test_client.py
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests# python3 -m unittest test_client.py
......
----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests#
```


# Task8 test_client.py

test_client.py
```python

```

```bash

```


# Task9 test_client.py

test_client.py
```python

```

```bash

```
