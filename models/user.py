#!/usr/bin/env python3
""""User class"""

from models.base_model import BaseModel

"""Inheritance: Base Model"""


class User(BaseModel):
    """All users details"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
