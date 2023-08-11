#!/usr/bin/python3

"""
makes class User
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    the user class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
