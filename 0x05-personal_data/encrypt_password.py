#!/usr/bin/env python3
""" 6. Check valid password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ hash_password
      - encrypt password
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    """
    return bcrypt.checkpw(bytes(password, 'utf-8'), hashed_password)
