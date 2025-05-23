#!/usr/bin/env python3
"""
Module to hash and validate passwords using bcrypt
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt with a salt"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates a password against its hashed version"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
