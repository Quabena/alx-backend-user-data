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
        return False

    def authorization_header(self, request=None) -> str:
        """Retrieves the authorization header from the request"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current user from the request"""
        return None
