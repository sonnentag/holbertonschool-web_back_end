#!/usr/bin/env python3
""" BasicAuth Module
"""

from api.v1.auth.auth import Auth
from base64 import b64decode, decode
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ BasicAuth Class
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ returns the Base64 part of the Authorization header
        """
        if authorization_header and type(authorization_header) is str:
            if authorization_header[0:6] == 'Basic ':
                return authorization_header[6:]
        return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ returns the decoded value of base64_authorization_header
        """
        if not base64_authorization_header:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = b64decode(base64_authorization_header, None, True)
        except Exception:
            return None
        return decoded.decode("utf-8")

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ returns the user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header:
            if isinstance(decoded_base64_authorization_header, str):
                if ':' in decoded_base64_authorization_header:
                    return decoded_base64_authorization_header.split(':', 1)
        return (None, None)

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ returns the User instance based on his email and password
        """
        if not user_email or not isinstance(user_email, str):
            return None
        if not user_pwd or not isinstance(user_pwd, str):
            return None
        users = User.search({'email': user_email})
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ overloads Auth and retrieves the User instance for a reques
        """
        auth_header = self.authorization_header(request)
        extract_header = self.extract_base64_authorization_header(auth_header)
        decode_header = self.decode_base64_authorization_header(
                b64_extracted_auth_header)
        user_credentials = self.extract_user_credentials(
                b64_decoded_auth_header)
        user_object = self.user_object_from_credentials(
                user_credentials[0], user_credentials[1])
        return user_object
