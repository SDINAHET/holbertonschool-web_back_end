#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict
# from 2-hypermedia_pagination import Server
Server = __import__('2-hypermedia_pagination').Server


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get a page of the dataset with deletion-resilient pagination.

        Args:
            index (int): The current start index.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing pagination metadata.
                -index: the current start index of the return page. That is the
                index of the first item in the current page. For example if
                requesting page 3 with page_size 20, and no data was removed
                from the dataset, the current index should be 60.
                -next_index: the next index to query with. That should be the
                index of the first item after the last item on the current page.
                -page_size: the current page size
                -data: the actual page of the dataset
        """
        assert isinstance(index, int) and 0 <= index < len(self.dataset())

        data = []
        current_index = index
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
