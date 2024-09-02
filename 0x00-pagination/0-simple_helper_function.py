#!/usr/bin/env python3
"""start to end"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function that returns start to end"""
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)
