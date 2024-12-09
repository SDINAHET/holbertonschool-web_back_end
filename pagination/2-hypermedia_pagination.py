#!/usr/bin/env python3
"""
Server class with hypermedia pagination.
"""
import math
from typing import Dict
# from 1-simple_pagination import Server
Server = __import__('1-simple_pagination').Server


class Server(Server):
    """Server class with hypermedia pagination."""

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get a page of the dataset with hypermedia metadata.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing pagination metadata.
                -page_size: the length of the returned dataset page
                -page: the current page number
                -data: the dataset page (equivalent to return from previous
                task)
                -next_page: number of the next page, None if no next page
                -prev_page: number of the previous page, None if no previous
                page
                -total_pages: the total number of pages in the dataset as an
                integer
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
