Unittests_and_integration_tests

```bash
$ python -m unittest path/to/test_file.py

python3 -m unittest test_utils.py
python3 -m unittest test_client.py

python3 -m venv .venv
source .venv/bin/activate
pip install parameterized

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
