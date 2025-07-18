#!/usr/bin/env python3
"""1. FIFO caching system"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache inherits from BaseCaching and implements
    a FIFO (First-In First-Out) caching system.
    """

    def __init__(self):
        """
        Initialize the cache by calling the parent constructor.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache using FIFO replacement policy.
        If key or item is None, do nothing.
        If cache is full, discard the first item added.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

            self.order.append(key)
        else:
            # Update order: keep original FIFO position
            pass

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve item from cache by key.
        Return None if key is None or not found.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
