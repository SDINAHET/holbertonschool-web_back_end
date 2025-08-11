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

# Task0

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


# Task1

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


# Task2

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
.......
----------------------------------------------------------------------
Ran 7 tests in 0.002s

OK
(.venv) root@UID7E:/mnt/d/Users/steph/Documents/5ème_trimestre/holbertonschool-web_back
_end/Unittests_and_integration_tests#
```


# Task3

test_utils.py
```python

```

```bash

```

# Task4

test_utils.py
```python

```

```bash

```


# Task4

test_utils.py
```python

```

```bash

```

# Task5

test_utils.py
```python

```

```bash

```


# Task6

test_utils.py
```python

```

```bash

```

# Task7

test_utils.py
```python

```

```bash

```


# Task8

test_utils.py
```python

```

```bash

```


# Task9

test_utils.py
```python

```

```bash

```
