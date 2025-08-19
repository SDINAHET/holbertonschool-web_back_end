#!/usr/bin/env python3
"""Basic Redis cache module.

Provides a `Cache` class that wraps a Redis client and exposes a `store`
method to persist primitive values (str, bytes, int, float) under a
randomly generated UUID key.
"""

from typing import Union
import uuid
import redis


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
