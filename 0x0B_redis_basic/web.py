#!/usr/bin/env python3
"""Expiring web cache and access counter using Redis (Task 5).

- get_page(url): fetches HTML via requests, caches it 10s in Redis,
  and increments a per-URL access counter at key "count:{url}".
"""

from typing import Optional
import redis
import requests

# Module-level Redis client (default: localhost:6379, db 0)
_redis = redis.Redis()


def get_page(url: str) -> str:
    """Return the HTML content for `url`, with Redis caching and counting.

    - Increments "count:{url}" on EVERY call (cache hit or miss).
    - If cached under key `url`, returns the cached HTML.
    - Otherwise fetches via HTTP, stores in cache with a 10-second TTL,
    returns it.

    Args:
        url: The URL to fetch.

    Returns:
        The page HTML content as a UTF-8 string.

    Raises:
        requests.HTTPError: If the HTTP response is not successful.
        requests.RequestException: For network-related errors.
    """
    # Track access count
    _redis.incr(f"count:{url}")

    # Try cache
    cached = _redis.get(url)
    if cached is not None:
        # Redis returns bytes -> decode to str (UTF-8)
        return cached.decode("utf-8")

    # Miss: fetch and cache
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    html: str = resp.text  # already str (decoded by requests)

    # Cache with 10s expiration
    _redis.setex(url, 10, html)
    return html
