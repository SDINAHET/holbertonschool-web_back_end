#!/usr/bin/env python3
"""Main file to test Task 1."""

Cache = __import__('exercise').Cache

cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    result = cache.get(key, fn=fn)
    print("IN:", value, "KEY:", key, "OUT:", result)
    assert result == value

# Tests directs des helpers
k1 = cache.store("hello")
assert cache.get_str(k1) == "hello"

k2 = cache.store("42")
assert cache.get_int(k2) == 42

print("✅ Task 1 OK")
