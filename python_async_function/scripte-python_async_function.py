# Script to create files for the specified tasks with their respective solutions

file_contents = {
    "0-basic_async_syntax.py": """#!/usr/bin/env python3
\"\"\"
This module defines an asynchronous coroutine `wait_random`.
\"\"\"

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    \"\"\"
    Wait for a random delay and return it.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: The random delay.
    \"\"\"
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
""",
    "1-concurrent_coroutines.py": """#!/usr/bin/env python3
\"\"\"
This module defines an async routine `wait_n` that spawns multiple coroutines.
\"\"\"

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    \"\"\"
    Spawn `wait_random` n times and return list of delays in ascending order.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    \"\"\"
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
""",
    "2-measure_runtime.py": """#!/usr/bin/env python3
\"\"\"
This module defines a function `measure_time` to measure runtime of `wait_n`.
\"\"\"

import time
from 1-concurrent_coroutines import wait_n

def measure_time(n: int, max_delay: int) -> float:
    \"\"\"
    Measure total execution time for `wait_n` and return average time.

    Args:
        n (int): Number of tasks.
        max_delay (int): Maximum delay for tasks.

    Returns:
        float: Average time per task.
    \"\"\"
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time
    return total_time / n
""",
    "3-tasks.py": """#!/usr/bin/env python3
\"\"\"
This module defines a function `task_wait_random` to create asyncio.Task.
\"\"\"

import asyncio
from 0-basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    \"\"\"
    Create and return an asyncio.Task.

    Args:
        max_delay (int): Maximum delay for wait_random.

    Returns:
        asyncio.Task: The created Task.
    \"\"\"
    return asyncio.create_task(wait_random(max_delay))
""",
    "4-tasks.py": """#!/usr/bin/env python3
\"\"\"
This module defines an async routine `task_wait_n` that spawns multiple tasks.
\"\"\"

import asyncio
from typing import List
from 3-tasks import task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    \"\"\"
    Spawn `task_wait_random` n times and return list of delays in ascending order.

    Args:
        n (int): Number of times to call task_wait_random.
        max_delay (int): Maximum delay for task_wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    \"\"\"
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
"""
}

# Create directory to store files
import os

directory = "python_async_function"
os.makedirs(directory, exist_ok=True)

# Write each file
for filename, content in file_contents.items():
    filepath = os.path.join(directory, filename)
    with open(filepath, "w") as f:
        f.write(content)

print(f"All files created in directory: {directory}")
