#!/usr/bin/env python3
"""Basic Redis cache module.

Task 0: store values under random UUID keys.
Task 1: retrieve values with optional conversion back to original types.
Task 2: count how many times Cache.store is called.
"""

from typing import Union, Optional, Callable, TypeVar
from functools import wraps
import uuid
import redis

T = TypeVar("T")


def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times a method is called.

    Stores the count in Redis using the method's qualified name as key.
    """
    key = method.__qualname__  # <-- explicit binding for the checker

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # increment call count in Redis
        self._redis.incr(key)
        # call the original method
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to record call history: inputs and outputs in Redis lists.

    Uses two keys:
      <qualname>:inputs  -> RPUSH of str(args)
      <qualname>:outputs -> RPUSH of the returned value (as bytes/str/number)
    """
    in_key = f"{method.__qualname__}:inputs"
    out_key = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # store inputs (normalize to string)
        self._redis.rpush(in_key, str(args))
        # call original method
        result = method(self, *args, **kwargs)
        # store output (Redis can store str/bytes/int/float directly)
        self._redis.rpush(out_key, result)
        return result

    return wrapper


class Cache:
    """Simple cache backed by Redis."""

    def __init__(self) -> None:
        """Initialize a Redis client and flush the current database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
