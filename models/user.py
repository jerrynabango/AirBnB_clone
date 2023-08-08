#!/usr/bin/env python3
""""User details"""

from models.base_model import BaseModel

"""Inheritance: Base Model"""


class User(BaseModel):
    """All users details"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
