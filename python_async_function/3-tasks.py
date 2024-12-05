#!/usr/bin/env python3
"""
This module defines a function `task_wait_random` to create asyncio.Task.
"""

import asyncio
# from 0-basic_async_syntax import wait_random
wait_random = __import__('0-basic_async_syntax').wait_random


# from 0-basic_async_syntax import wait_random
# wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task.

    Args:
        max_delay (int): Maximum delay for wait_random.

    Returns:
        asyncio.Task: The created Task.
    """
    return asyncio.create_task(wait_random(max_delay))

# import asyncio
# from 0_basic_async_syntax import wait_random

# def task_wait_random(max_delay: int) -> asyncio.Task:
#     return asyncio.create_task(wait_random(max_delay))
