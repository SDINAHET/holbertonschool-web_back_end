#!/usr/bin/env python3
"""
Module for filtering sensitive data using regex
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    return re.sub(rf'({"|".join(fields)})=.*?{separator}', lambda m: f"{m.group(1)}={redaction}{separator}", message)
