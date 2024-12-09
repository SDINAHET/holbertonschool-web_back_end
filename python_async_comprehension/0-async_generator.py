#!/usr/bin/env python3
"""
Module contenant une coroutine génératrice asynchrone.
"""
import asyncio
import random


from typing import AsyncGenerator


# async def async_generator() -> AsyncGenerator[float, None]:
async def async_generator():
    """
    Génère 10 nombres aléatoires entre 0 et 10, avec une pause de 1 seconde
    entre chaque.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
