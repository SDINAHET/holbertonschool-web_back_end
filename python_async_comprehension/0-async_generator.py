#!/usr/bin/env python3
"""
Module containing an asynchronous generator that yields random numbers.
Module contenant une coroutine génératrice asynchrone.
"""
import asyncio
import random
# from typing import AsyncGenerator
# from typing import async_generator
# import typing
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    Génère 10 nombres aléatoires entre 0 et 10, avec une pause de 1 seconde
    entre chaque.
    A coroutine that generates 10 random numbers asynchronously.
    Each number is between 0 and 10, with a 1-second delay between generations.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
