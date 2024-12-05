#!/usr/bin/env python3
"""
This module defines an async routine `wait_n` that spawns multiple coroutines.
"""

import asyncio


from typing import List
# from 0-basic_async_syntax import wait_random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn `wait_random` n times and return list of delays in ascending order.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)

# import asyncio
# from 0_basic_async_syntax import wait_random

# async def wait_n(n, max_delay):
#     tasks = [wait_random(max_delay) for _ in range(n)]
#     delays = await asyncio.gather(*tasks)
#     return delays
