#!/usr/bin/env python3
"""
Personal data
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """ Hash password
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validate password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
