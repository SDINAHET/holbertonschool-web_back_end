#!/usr/bin/env python3
"""3. LRU caching system"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache inherits from BaseCaching and implements
    an LRU (Least Recently Used) caching system.
    """

    def __init__(self):
        """Initialize the cache and usage tracker"""
        super().__init__()
        self.usage_order = []  # keeps track of usage order (most recent at end

    def put(self, key, item):
        """
        Add an item to the cache using LRU replacement policy.
        If key or item is None, do nothing.
        If the cache is full, discard the least recently used item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the value and usage position
            self.cache_data[key] = item
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove least recently used
                lru_key = self.usage_order.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)

            self.cache_data[key] = item
            self.usage_order.append(key)

    def get(self, key):
        """
        Retrieve an item by key and mark it as recently used.
        Return None if key is None or not found.
        """
        if key is None or key not in self.cache_data:
            return None

        # Move key to the end to mark it as recently used
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
