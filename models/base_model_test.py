#!/usr/bin/python3
"""module base model"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """base model"""
    def __init__(self, *args, **kwargs):
        """type method init"""
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or "updated_at":
                    setattr(self, key, datetime.strptime(value, timeformat))
                elif key != '__class__':
                    setattr(self, key, value)
        else:           
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

        def __str__(self):
            """ Type method __str__ """
            class_name = self.__class__.__name__
            return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

        def save(self):
            """ Update the attribute update_at with current datetime """
            self.updated_at = datetime.today

        def to_dict(self):
            lildict = self.__dict__.copy()
            lildict["created_at"] = datetime.created_at.isoformat()
            lildict["updated_at"] = datetime.updated_at.isoformat()
            lildict["__class__"] = self.__class__.__name__
            return lildict
