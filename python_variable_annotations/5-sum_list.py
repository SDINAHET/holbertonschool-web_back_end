#!/usr/bin/env python3
"""
This module defines a function `sum_list` that sums a list of floats.
5-sum_list.py
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sum a list of floats.

    Args:
        input_list (List[float]): A list of floats.

    Returns:
        float: The sum of the floats.
    """
    return sum(input_list)
