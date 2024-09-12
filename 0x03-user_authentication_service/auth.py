#!/usr/bin/env python3

"""Auth module"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Hash a password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """initiates the class"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a user to the database"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists.")
        except NoResultFound:
            hashed_password = _hash_password(password)
            self._db.add_user(email=email,
                              hashed_password=hashed_password)
            return self._db.find_user_by(email=email)

    def valid_login(self, email: str, password: str) -> bool:
        """validates login"""
        try:
            user = self.find_user_by(email=email)
            if user and user.hashed_password:
                return bcrypt.checkpw(password.encode('utf-8'),
                                      user.hashed_password)
        except Exception:
            return False
        return False
