#!/usr/bin/env python3
"""
Module for filtering sensitive data using regex
"""

import re
import logging
from typing import List
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection


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


# PII fields from user_data.csv
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger for user data with sensitive fields
    redacted.

    Returns:
        A logging.Logger object configured with RedactingFormatter.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger


def get_db():
    """
    Connects to a secure MySQL database using credentials from environment
    variables.

    Returns:
        MySQLConnection object to the database.
    """
    return mysql.connector.connect(
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )


def main():
    """
    Main function to read users from database and log each row
    with PII fields redacted.

    The function:
    - Connects to the database using get_db().
    - Retrieves all rows from the users table.
    - Logs each row with sensitive fields redacted using a logger.
    - Closes the cursor and the database connection using cursor.close()
      and db.close().
    """
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users;")
    field_names = [i[0] for i in cursor.description]

    logger = get_logger()

    for row in cursor:
        message = ''.join(f"{k}={v}; " for k, v in zip(
            field_names, row)).strip()
        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
