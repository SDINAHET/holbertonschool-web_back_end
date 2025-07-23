#!/usr/bin/env python3
"""
Module for filtering sensitive data using regex
"""

import re
import logging
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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class to obfuscate sensitive fields in logs """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with specific fields to redact.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record, redacting sensitive data.
        """
        original = super().format(record)
        return filter_datum(
            self.fields, self.REDACTION, original, self.SEPARATOR)
