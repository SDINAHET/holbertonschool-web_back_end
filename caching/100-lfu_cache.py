#!/usr/bin/env python3
"""5. LFU caching system"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache implements a Least Frequently Used (LFU) caching system.
    If frequency is equal, Least Recently Used (LRU) is used as a tie-breaker.
    """

    def __init__(self):
        """Initialize the LFU cache"""
        super().__init__()
        self.freq = {}         # frequency of each key
        self.usage_order = []  # LRU fallback in case of tie

    def put(self, key, item):
        """
        Add item to cache.
        If cache exceeds MAX_ITEMS, discard LFU item.
        If tie in frequency, discard LRU among them.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find minimum frequency
                min_freq = min(self.freq.values())
                # List of keys with min freq
                lfu_keys = [k for k in self.freq if self.freq[k] == min_freq]
                # Use LRU among LFU keys
                for k in self.usage_order:
                    if k in lfu_keys:
                        discard_key = k
                        break
                # Remove from cache
                del self.cache_data[discard_key]
                del self.freq[discard_key]
                self.usage_order.remove(discard_key)
                print("DISCARD:", discard_key)

            self.cache_data[key] = item
            self.freq[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        """
        Retrieve item and increase usage frequency.
        """
        if key is None or key not in self.cache_data:
            return None

        self.freq[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
