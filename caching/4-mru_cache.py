#!/usr/bin/env python3
"""4. MRU caching system"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache inherits from BaseCaching and implements
    a MRU (Most Recently Used) caching system.
    """

    def __init__(self):
        """Initialize the cache and usage tracker"""
        super().__init__()
        self.usage_order = []  # Most recently used at end

    def put(self, key, item):
        """
        Add an item to the cache using MRU replacement policy.
        If key or item is None, do nothing.
        If cache is full, discard the most recently used item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove most recently used key (last in usage_order)
                mru_key = self.usage_order.pop()
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)

            self.cache_data[key] = item
            self.usage_order.append(key)

    def get(self, key):
        """
        Retrieve an item by key and mark it as most recently used.
        Return None if key is None or not found.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update usage order to mark key as most recently used
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
