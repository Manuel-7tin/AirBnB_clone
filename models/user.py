#!usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """A class that inherits from basemodel to store user details"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
