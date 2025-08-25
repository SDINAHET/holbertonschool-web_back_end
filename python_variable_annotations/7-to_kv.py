#!/usr/bin/env python3
"""
This module defines a function `to_kv` that returns a tuple with a string and
the square of a number.
7-to_kv.py
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple with a string and the square of a number.

    Args:
        k (str): The input string.
        v (Union[int, float]): An integer or float.

    Returns:
        Tuple[str, float]: A tuple where the first element is k and the second
        is v squared.
    """
    return (k, float(v**2))
