#!/usr/bin/env python3
"""0. Basic dictionary caching system"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache inherits from BaseCaching and is a basic caching system
    with no item limit.
    """

    def put(self, key, item):
        """
        Add an item in the cache_data dictionary.

        If key or item is None, do nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key from cache_data.

        Returns None if key is None or doesn’t exist.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
