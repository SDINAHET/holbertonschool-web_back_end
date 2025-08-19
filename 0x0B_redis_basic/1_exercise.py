#!/usr/bin/env python3
"""Basic Redis cache module.

Task0
Provides a `Cache` class that wraps a Redis client and exposes a `store`
method to persist primitive values (str, bytes, int, float) under a
randomly generated UUID key.

Task1
Defines a Cache class to store values in Redis with random UUID keys and
retrieve them with optional conversion back to the original type.
"""

from typing import Union, Optional, Callable, TypeVar
import uuid
import redis

T = TypeVar("T")


class Cache:
    """Simple cache backed by Redis."""

    def __init__(self) -> None:
        """Initialize a Redis client and flush the current database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store a value in Redis under a random UUID key.

        Args:
            data: Value to store (str, bytes, int, or float).

        Returns:
            The UUID key (as a string) used to store the value.
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], T]] = None) -> Optional[Union[bytes, T]]:
        """Retrieve a value from Redis and optionally convert it.

        Args:
            key: Redis key to fetch.
            fn: Optional callable that converts the raw bytes into the desired
                type (e.g., int, float, lambda d: d.decode("utf-8"), etc.).

        Returns:
            - None if the key does not exist (mirrors Redis.get behavior).
            - Raw bytes if `fn` is None and the key exists.
            - Converted value of type T if `fn` is provided.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a value as UTF-8 string (or None if missing)."""
        data = self.get(key, fn=lambda d: d.decode("utf-8"))
        return data  # type: ignore[return-value]

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve a value converted to int (or None if missing)."""
        data = self.get(key, fn=int)
        return data  # type: ignore[return-value]
