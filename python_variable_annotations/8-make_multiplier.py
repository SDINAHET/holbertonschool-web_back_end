#!/usr/bin/env python3
"""
This module defines a function `make_multiplier` that creates a multiplier
function.
8-make_multiplier.py
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that multiplies a float by the
        multiplier.
    """
    return lambda x: x * multiplier
