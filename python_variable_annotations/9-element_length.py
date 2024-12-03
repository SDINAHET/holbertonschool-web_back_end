#!/usr/bin/python3
"""
This module defines a function `element_length` that returns a list of tuples
with an element and its length.
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Get a list of tuples with an element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples with each element and its length.
    """
    return [(i, len(i)) for i in lst]
