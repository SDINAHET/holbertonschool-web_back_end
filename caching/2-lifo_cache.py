#!/usr/bin/env python3
"""2. LIFO caching system"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache inherits from BaseCaching and implements
    a LIFO (Last-In First-Out) caching system.
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.last_key = None  # keep track of last inserted key

    def put(self, key, item):
        """
        Add an item to the cache using LIFO replacement policy.

        If the cache exceeds MAX_ITEMS, discard the last inserted item.
        """
        if key is None or item is None:
            return
        if (
            key not in self.cache_data and
            len(self.cache_data) >= BaseCaching.MAX_ITEMS
        ):
            # Remove last inserted key (not necessarily the last in the dict)
            if self.last_key in self.cache_data:
                del self.cache_data[self.last_key]
                print("DISCARD:", self.last_key)

        self.cache_data[key] = item
        self.last_key = key  # update last inserted key

    def get(self, key):
        """
        Retrieve item from cache by key.

        Return None if key is None or not found.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
