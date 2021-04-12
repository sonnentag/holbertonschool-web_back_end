#!/usr/bin/env python3
""" Auth module
"""

from flask import request
from typing import List, TypeVar


class Auth():
    """ Auth Class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth returns false if path is excluded
        """
        if not path or not excluded_paths or excluded_paths is []:
            return True
        if path[len(path) - 1] is not '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ returns auth header
        """
        if request and request.headers.get('Authorization'):
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns None for now
        """
        return None

    def session_cookie(self, request=None):
        """ Return current session cookie
        """
        if request:
            return request.cookies.get(os.getenv("SESSION_NAME"))
        return None
