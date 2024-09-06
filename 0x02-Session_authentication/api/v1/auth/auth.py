#!/usr/bin/env python3
"""
Auth module
"""

from flask import request
from typing import List, TypeVar
import os



class Auth():
    """
    Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Require auth
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path in excluded_paths:
            return False

        if not path.endswith('/'):
            path += '/'

        for ex_path in excluded_paths:
            if ex_path.endswith('*'):
                if path.startswith(ex_path[:-1]):
                    return False
            else:
                if not ex_path.endswith('/'):
                    ex_path += '/'
                if path == ex_path:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Authorization header
        """
        if request is None:
            return None
        auth_h = request.headers.get('Authorization')
        if auth_h is None:
            return None

        return auth_h

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Current user
        """
        return None

    def session_cookie(self, request=None):
        """
        Session cookie
        """
        if request is None:
            return None

        _my_session_id = os.getenv('SESSION_NAME')
        return request.cookies.get(_my_session_id)