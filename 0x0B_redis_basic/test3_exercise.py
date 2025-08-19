#!/usr/bin/env python3
"""Unit tests for Task 3 (call_history) of 0x0B_redis_basic."""

import unittest
import redis
from exercise import Cache  # ATTENTION: 'exercise', pas 'exercice'


class TestCallHistoryTask3(unittest.TestCase):
    """Tests for recording inputs/outputs history with call_history."""

    def setUp(self):
        self.cache = Cache()
        self.r = redis.Redis()
        self.r.flushdb()  # base propre
        self.qual = self.cache.store.__qualname__
        self.in_key = f"{self.qual}:inputs"
        self.out_key = f"{self.qual}:outputs"

    def test_history_is_empty_initially(self):
        self.assertEqual(self.r.lrange(self.in_key, 0, -1), [])
        self.assertEqual(self.r.lrange(self.out_key, 0, -1), [])

    def test_inputs_and_outputs_recorded(self):
        k1 = self.cache.store("first")
        k2 = self.cache.store("secont")
        k3 = self.cache.store("third")

        inputs = self.r.lrange(self.in_key, 0, -1)
        outputs = self.r.lrange(self.out_key, 0, -1)

        self.assertEqual(inputs, [b"('first',)", b"('secont',)", b"('third',)"])
        self.assertEqual(outputs, [k1.encode(), k2.encode(), k3.encode()])

    def test_mixed_types(self):
        k1 = self.cache.store("txt")
        k2 = self.cache.store(b"bytes")
        k3 = self.cache.store(123)
        k4 = self.cache.store(3.14)

        inputs = self.r.lrange(self.in_key, -4, -1)
        outputs = self.r.lrange(self.out_key, -4, -1)

        self.assertEqual(inputs, [b"('txt',)", b"(b'bytes',)", b'(123,)', b'(3.14,)'])
        self.assertEqual(outputs, [k1.encode(), k2.encode(), k3.encode(), k4.encode()])

    def test_count_calls_still_increments(self):
        counter_key = self.cache.store.__qualname__
        self.assertIsNone(self.r.get(counter_key))
        self.cache.store("one")
        self.cache.store("two")
        self.assertEqual(self.r.get(counter_key), b"2")


if __name__ == "__main__":
    unittest.main()
