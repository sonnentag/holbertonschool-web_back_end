#!/usr/bin/env python3
""" SessionAuth module """

from api.v1.auth.auth import Auth
from uuid import uuid4
import os


class SessionAuth(Auth):
    """ SessionAuth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create new session
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Return user id of current user
        """
        if session_id is None or not isinstance(user_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def session_cookie(self, request=None):
        """ Return current session cookie
        """
        if request:
            return request.cookies.get(os.getenv("SESSION_NAME"))
        return None
