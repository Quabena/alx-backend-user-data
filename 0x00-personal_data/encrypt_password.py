#!/usr/bin/env python3
"""
Module to hash passwords using bcrypt
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt with a salt"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
