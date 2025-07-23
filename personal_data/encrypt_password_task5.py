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
