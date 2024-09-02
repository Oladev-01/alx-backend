#!/usr/bin/env python3
"""start to end"""
import csv
import math
from typing import List, Dict, Any

class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the appropriate page of the dataset."""
        if not isinstance(page, int) or not isinstance(page_size, int):
            raise ValueError("Page and page_size must be integers")
        
        if page <= 0 or page_size <= 0:
            raise ValueError("Page and page_size must be positive integers")

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []  # Return an empty list if the start index is out of range

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Returns a dictionary with hypermedia pagination information."""
        data = self.get_page(page, page_size)
        total_data = len(self.dataset())
        total_pages = math.ceil(total_data / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple of the start and end index corresponding to the range of indexes."""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
