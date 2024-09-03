#!/usr/bin/env python3
"""
Auth module
"""

from flask import request
from typing import List, TypeVar


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

        if excluded_paths is None or excluded_paths == []:
            return True

        if path in excluded_paths:
            return False

        if path[-1] != '/':
            path += '/'

        for ex_path in excluded_paths:
            if ex_path[-1] != '/':
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
        if request.headers.get('Authorization') is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Current user
        """
        return None
