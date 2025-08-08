#!/usr/bin/env python3
import unittest
import uuid
from unittest.mock import patch
from auth import _generate_uuid


class TestGenerateUUID(unittest.TestCase):
    def test_returns_string_and_valid_uuid(self):
        """Should return a str that is a valid UUIDv4"""
        s = _generate_uuid()
        self.assertIsInstance(s, str)

        # Do we parse as UUID v4?
        parsed = uuid.UUID(s, version=4)
        self.assertEqual(parsed.version, 4)
        # Ensure the string is exactly the canonical hex format with hyphens
        self.assertEqual(str(parsed), s)

    def test_returns_different_values_each_time(self):
        """Two calls should not return the same UUID"""
        s1 = _generate_uuid()
        s2 = _generate_uuid()
        self.assertNotEqual(s1, s2)

    def test_uses_uuid4_under_the_hood(self):
        """Patch uuid.uuid4 to a fixed value and ensure it is returned as str"""
        fixed = uuid.UUID("163fe508-19a2-48ed-a7c8-d9c6e56fabd1")
        with patch("auth.uuid.uuid4", return_value=fixed) as mock_uuid4:
            s = _generate_uuid()
            self.assertEqual(s, str(fixed))
            mock_uuid4.assert_called_once()


if __name__ == "__main__":
    unittest.main(verbosity=2)
