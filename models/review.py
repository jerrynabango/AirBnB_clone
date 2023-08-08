#!/usr/bin/env python3
"""Review class"""

from models.base_model import BaseModel

""""Inheritance: BaseModel"""


class Review(BaseModel):
    """All review details"""
    place_id = ""
    user_id = ""
    text = ""
