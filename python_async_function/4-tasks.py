#!/usr/bin/env python3
"""
This module defines an async routine `task_wait_n` that spawns multiple tasks.
"""

import asyncio
from typing import List
# from 3-tasks import task_wait_random
task_wait_random = __import__('3-tasks').task_wait_random


# from 0-basic_async_syntax import wait_random
# wait_random = __import__('0-basic_async_syntax').wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn `task_wait_random` n times and return list of delays in ascending
    order.

    Args:
        n (int): Number of times to call task_wait_random.
        max_delay (int): Maximum delay for task_wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)

# import asyncio
# from 3_tasks import task_wait_random

# async def task_wait_n(n, max_delay):
#     tasks = [task_wait_random(max_delay) for _ in range(n)]
#     delays = await asyncio.gather(*tasks)
#     return delays
