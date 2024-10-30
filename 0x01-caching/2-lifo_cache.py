#!/usr/bin/env python3
"""
Module that provides LIFOCache class.
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO Caching system.
    """
    def __init__(self):
        """
        Initialize parent class
        """
        super().__init__()
        # Initialize a list to keep track of the order of keys for LIFO
        self.keys = []

    def put(self, key, item):
        """
        Assign item value to a key in the dictionary.
        If the cache exceeds MAX_ITEMS, remove the last added item (LIFO).
        """
        if key is None or item is None:
            return

        self.keys.append(key)
        self.cache_data[key] = item

        # Check if we need to discard the last item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = self.keys.pop(-2)
            # Remove it from the cache
            del self.cache_data[discard]
            print(f"DISCARD: {discard}")

    def get(self, key):
        """
        Return value in the dictionary by key.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
