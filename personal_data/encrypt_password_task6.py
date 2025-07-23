#!/usr/bin/env python3
"""
Module to securely hash passwords using bcrypt
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with automatic salting.

    Args:
        password: The password to hash.

    Returns:
        A salted, hashed password as bytes.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates that the provided password matches the hashed password.

    Args:
        hashed_password: The previously hashed password (as bytes).
        password: The plain-text password to validate.

    Returns:
        True if password is correct, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
