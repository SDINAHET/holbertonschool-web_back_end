#!/usr/bin/env python3
"""Unit tests for Task 1 of 0x0B_redis_basic."""

import unittest
import redis
from exercise import Cache


class TestCacheTask1(unittest.TestCase):
    """Unit tests for Cache.get, get_str, get_int."""

    def setUp(self):
        self.cache = Cache()
        self.r = redis.Redis()

    def test_get_returns_none_for_missing_key(self):
        """get should return None if key does not exist (Redis behavior)."""
        self.assertIsNone(self.cache.get("non-existent-key"))
        self.assertIsNone(self.cache.get_str("non-existent-key"))
        self.assertIsNone(self.cache.get_int("non-existent-key"))

    def test_get_without_fn_returns_bytes(self):
        """get without fn should return raw bytes."""
        k = self.cache.store("bar")
        val = self.cache.get(k)
        self.assertIsInstance(val, (bytes,))
        self.assertEqual(val, b"bar")

    def test_get_with_lambda_to_str(self):
        """get with a lambda decoder should round-trip a string."""
        k = self.cache.store("hello")
        out = self.cache.get(k, fn=lambda d: d.decode("utf-8"))
        self.assertEqual(out, "hello")

    def test_get_int_conversion(self):
        """get with int and get_int should convert bytes to int."""
        k1 = self.cache.store(123)
        self.assertEqual(self.cache.get(k1, fn=int), 123)

        k2 = self.cache.store("456")
        self.assertEqual(self.cache.get_int(k2), 456)

    def test_examples_from_statement(self):
        """Validate the examples provided in the instructions."""
        TEST_CASES = {
            b"foo": None,
            123: int,
            "bar": lambda d: d.decode("utf-8"),
        }
        for value, fn in TEST_CASES.items():
            key = self.cache.store(value)
            if fn is None:
                self.assertEqual(self.cache.get(key), value if isinstance(value, bytes) else str(value).encode())
            else:
                self.assertEqual(self.cache.get(key, fn=fn), value)


if __name__ == "__main__":
    unittest.main()
