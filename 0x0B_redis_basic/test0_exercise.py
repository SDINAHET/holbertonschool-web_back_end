#!/usr/bin/env python3
"""Unit tests for Task 0 of 0x0B_redis_basic."""

import unittest
import redis
from exercise import Cache


class TestCache(unittest.TestCase):
    """Unit tests for the Cache class (task 0)."""

    def setUp(self):
        """Create a fresh Cache instance before each test."""
        self.cache = Cache()
        self.redis = redis.Redis()

    def test_store_returns_string_key(self):
        """store should return a string key."""
        key = self.cache.store(b"hello")
        self.assertIsInstance(key, str)

    def test_store_and_retrieve_bytes(self):
        """Bytes should be stored and retrieved correctly from Redis."""
        key = self.cache.store(b"world")
        self.assertEqual(self.redis.get(key), b"world")

    def test_store_and_retrieve_str(self):
        """String should be stored and retrieved as bytes (UTF-8)."""
        key = self.cache.store("holberton")
        self.assertEqual(self.redis.get(key), b"holberton")

    def test_store_and_retrieve_int(self):
        """Int should be stored and retrieved as bytes."""
        key = self.cache.store(42)
        self.assertEqual(self.redis.get(key), b"42")

    def test_store_and_retrieve_float(self):
        """Float should be stored and retrieved as bytes."""
        key = self.cache.store(3.14)
        self.assertEqual(self.redis.get(key), b"3.14")


if __name__ == "__main__":
    unittest.main()
