#!/usr/bin/env python3
"""
Auth Module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Template for all authentication system"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determines if authentication is required for a given path"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        # Normalize path to ensure it ends with '/'
        if not path.endswith('/'):
            path += '/'

        for ex_path in excluded_paths:
            if ex_path == path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Retrieves the authorization header from the request"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current user from the request"""
        return None
