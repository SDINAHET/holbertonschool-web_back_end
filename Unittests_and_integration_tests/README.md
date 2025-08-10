Unittests_and_integration_tests

```bash
$ python -m unittest path/to/test_file.py

python3 -m unittest test_utils.py
python3 -m unittest test_client.py

python3 -m venv .venv
source .venv/bin/activate
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

```

```bash

```


# Task2

test_utils.py
```python

```

```bash

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
