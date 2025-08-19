#!/usr/bin/env python3
"""Unit tests for Task 4 (replay) of 0x0B_redis_basic."""

import io
import re
import unittest
from contextlib import redirect_stdout
from exercise import Cache, replay

UUID_RE = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
)


class TestReplayTask4(unittest.TestCase):
    def test_replay_output_format_and_values(self):
        cache = Cache()  # flushdb in __init__
        k1 = cache.store("foo")
        k2 = cache.store("bar")
        k3 = cache.store(42)

        buf = io.StringIO()
        with redirect_stdout(buf):
            replay(cache.store)
        lines = [line.rstrip("\n") for line in buf.getvalue().splitlines()]

        # 1) En-tête
        self.assertEqual(lines[0], "Cache.store was called 3 times:")

        # 2) Corps: 3 lignes, dans l'ordre
        self.assertTrue(lines[1].startswith("Cache.store(*('foo',)) -> "))
        self.assertTrue(lines[2].startswith("Cache.store(*('bar',)) -> "))
        self.assertTrue(lines[3].startswith("Cache.store(*(42,)) -> "))

        # 3) Extraire les UUID affichés
        u1 = lines[1].split(" -> ")[1]
        u2 = lines[2].split(" -> ")[1]
        u3 = lines[3].split(" -> ")[1]

        # 4) Vérifier que ce sont des UUID valides
        self.assertTrue(UUID_RE.match(u1))
        self.assertTrue(UUID_RE.match(u2))
        self.assertTrue(UUID_RE.match(u3))

        # 5) Vérifier que ce sont EXACTEMENT les clés renvoyées par store
        self.assertEqual([u1, u2, u3], [k1, k2, k3])


if __name__ == "__main__":
    unittest.main(verbosity=2)
