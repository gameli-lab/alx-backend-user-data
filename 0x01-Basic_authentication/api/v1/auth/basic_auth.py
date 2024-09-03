#!/usr/bin/env python3
"""
Basic Auth
"""

from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """
    Basic Auth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """
        Extract base64
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        Decode base64
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            auth = base64.b64decode(base64_authorization_header)
        except Exception:
            return None
        return auth.decode('utf-8')

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """
        Extract user credentials
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if decoded_base64_authorization_header.count(':') != 1:
            return None, None

        credentials = decoded_base64_authorization_header.split(':', 1)
        return credentials[0], credentials[1]

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str
                                     ) -> TypeVar('User'):
        """
        User object from credentials
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({'email': user_email})
        if not users:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None
