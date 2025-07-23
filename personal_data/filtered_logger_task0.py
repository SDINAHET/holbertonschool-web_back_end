#!/usr/bin/env python3
"""
Module for filtering sensitive data using regex
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields: list of field names to obfuscate.
        redaction: string used to replace the field values.
        message: the log message to filter.
        separator: the character separating key-value pairs.

    Returns:
        The filtered log message with sensitive fields obfuscated.
    """
    pattern = rf'({"|".join(fields)})=.*?{separator}'
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}{separator}",
                  message)
