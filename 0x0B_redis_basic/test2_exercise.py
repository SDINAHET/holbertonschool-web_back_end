#!/usr/bin/env python3
"""Unit tests for Task 2 (count_calls decorator) of 0x0B_redis_basic."""

import unittest
import redis
from exercise import Cache


class TestCountCallsTask2(unittest.TestCase):
    """Tests for the count_calls decorator applied to Cache.store."""

    def setUp(self):
        """Fresh Cache and Redis before each test."""
        self.cache = Cache()
        self.r = redis.Redis()
        # The Cache __init__ already flushes DB, but ensure clean state:
        self.r.flushdb()

    def test_store_count_increments(self):
        """Calling store should increment the counter key each time."""
        counter_key = self.cache.store.__qualname__

        # No calls yet -> counter should be None (missing key)
        self.assertIsNone(self.r.get(counter_key))

        # 1st call
        self.cache.store(b"first")
        self.assertEqual(self.r.get(counter_key), b"1")

        # 2nd & 3rd calls
        self.cache.store(b"second")
        self.cache.store(b"third")
        self.assertEqual(self.r.get(counter_key), b"3")

    def test_multiple_sequences(self):
        """Counter should reset on new Cache (flushdb in __init__)."""
        counter_key = self.cache.store.__qualname__

        # First sequence: 2 calls
        self.cache.store("A")
        self.cache.store("B")
        self.assertEqual(self.r.get(counter_key), b"2")

        # New cache flushes DB -> counter disappears -> starts from 1 again
        c2 = Cache()
        r2 = redis.Redis()
        counter_key_2 = c2.store.__qualname__

        self.assertIsNone(r2.get(counter_key_2))
        c2.store("C")
        self.assertEqual(r2.get(counter_key_2), b"1")

    def test_store_returns_key_and_sets_value(self):
        """Sanity check: store still returns a key and writes the value."""
        key = self.cache.store(b"hello")
        self.assertIsInstance(key, str)
        self.assertEqual(self.r.get(key), b"hello")

    def test_counter_key_is_qualname(self):
        """The counter should use the qualified name of the method as key."""
        counter_key = self.cache.store.__qualname__
        self.cache.store("x")
        self.assertTrue(self.r.exists(counter_key))


if __name__ == "__main__":
    unittest.main()
