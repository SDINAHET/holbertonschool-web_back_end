#!/usr/bin/env python3
"""
Server class with deletion-resilient hypermedia pagination.
"""
from typing import Dict
# from 2-hypermedia_pagination import Server
Server = __import__('2-hypermedia_pagination').Server


class Server(Server):
    """Server class with deletion-resilient hypermedia pagination."""

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get a page of the dataset with deletion-resilient pagination.

        Args:
            index (int): The current start index.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing pagination metadata.
        """
        assert isinstance(index, int) and 0 <= index < len(self.dataset())

        data = []
        next_index = index

        for _ in range(page_size):
            if next_index >= len(self.dataset()):
                break
            data.append(self.dataset()[next_index])
            next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
