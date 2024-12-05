#!/usr/bin/env python3
"""
This module defines a function `measure_time` to measure runtime of `wait_n`.
"""

import asyncio
import time
# from 1-concurrent_coroutines import wait_n
wait_n = __import__('1-concurrent_coroutines').wait_n


# from 0-basic_async_syntax import wait_random
# wait_random = __import__('0-basic_async_syntax').wait_random

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure total execution time for `wait_n` and return average time.

    Args:
        n (int): Number of tasks.
        max_delay (int): Maximum delay for tasks.

    Returns:
        float: Average time per task.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time
    return total_time / n

# import asyncio
# import time
# from 1_concurrent_coroutines import wait_n

# def measure_time(n, max_delay):
#     start_time = time.time()  # Record the start time
#     asyncio.run(wait_n(n, max_delay))  # Run the wait_n coroutine
#     end_time = time.time()  # Record the end time
#     total_time = end_time - start_time  # Calculate total execution time
#     return total_time / n  # Return the average time per call
