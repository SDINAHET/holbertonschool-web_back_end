#!/usr/bin/env python3
"""
Module contenant une compréhension asynchrone.
"""
from typing import List
# from 0_async_generator import async_generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collecte 10 nombres aléatoires depuis async_generator en utilisant une
    compréhension asynchrone.
    """
    return [num async for num in async_generator()]

    """random_numbers = [number async for number in async_generator()]
    return random_numbers[:10] """
