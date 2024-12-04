#!/usr/bin/env python3
"""
This module defines a function `sum_mixed_list` that sums a list of integers
and floats.
6-sum_mixed_list.py
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of the numbers as a float.
    """
    return sum(mxd_lst)
