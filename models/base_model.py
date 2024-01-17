#!/usr/bin/python3

"""BaseMode1 module"""

import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue  # Skip __class__ attribute
                if key in ['created_at', 'updated_at']:
                    setattr(
                            self,
                            key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                            )
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """String representation of BaseModel."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id, self.__dict__
                )

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def from_dict(self, dict_data):
        """Create instance from dictionary data"""
        pass
