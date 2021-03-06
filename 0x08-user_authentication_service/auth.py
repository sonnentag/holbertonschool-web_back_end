#!/usr/bin/env python3
""" Auth module
"""

import bcrypt
from user import User
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> str:
    """ hash password
    """
    return bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt())


def _generate_uuid() -> str:
    """ generate uuid
    """
    return str(uuid4())


class Auth:
    """ Auth class to interact with the authentication database.
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ register user
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            pwd_encrypt = _hash_password(password=password)
            return self._db.add_user(email=email, hashed_password=pwd_encrypt)
        else:
            raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """ valid login
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        else:
            return bcrypt.checkpw(password=password.encode(),
                                  hashed_password=user.hashed_password)

    def create_session(self, email: str) -> str:
        """ create session
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        else:
            user.session_id = _generate_uuid()

            return user.session_id

    def get_user_from_session_id(self, session_id: str) -> str:
        """ get user from session_id
        """
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

        if user.session_id is None:
            return None
        else:
            return user

    def destroy_session(self, user_id: int) -> None:
        """ destroy the session
        """
        try:
            user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None

        user.session_id = None

    def get_reset_password_token(self, email: str) -> str:
        """ get reset password token
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        user.reset_token = _generate_uuid()

        return user.reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """ update password
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        else:
            user.hashed_password = _hash_password(password=password)
            user.reset_token = None
