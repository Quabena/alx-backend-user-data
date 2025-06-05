#!/usr/bin/env python3
"""
This module defines the User model using SQLAlchemy's declarative system.
It maps to a database table named 'users' and stores user authentication data.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from typing import Optional

Base = declarative_base()


class User(Base):
    """
    Represents a user of the system.
    Stores essential authentication and session data for each user.
    """
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(250), nullable=False)
    hashed_password: str = Column(String(250), nullable=False)
    session_id: Optional[str] = Column(String(250), nullable=True)
    reset_token: Optional[str] = Column(String(250), nullable=True)
