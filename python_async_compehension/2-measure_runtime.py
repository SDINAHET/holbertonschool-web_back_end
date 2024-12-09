#!/usr/bin/env python3
"""
Module pour mesurer le temps d'exécution de tâches parallèles.
"""
import asyncio
import time

from 1_async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Exécute async_comprehension quatre fois en parallèle et mesure le temps
    total.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start_time
