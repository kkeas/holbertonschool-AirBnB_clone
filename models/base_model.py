#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    """Represent a class BaseModel that defines
    all attributes/methods for other classes"""
    
    
    def __init__(self, *args, **kwargs):
    self.id = str(uuid.uuid4())
    self.created_at = datetime.now()
    self.updated_at = datetime.now()
    
    if kwargs:
        for key, value in kwargs.items():
            if key == "created_at":
                self.created_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            elif key == "updated_at":
                self.updated_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            elif key != "__class__":
                setattr(self, key, value)
                
    def __str__(self):
        return "[{}] ({}) {}".format(
            type(self).__name__,
            self.id,
            self.__dict__
        )
    
    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):
        new_dict = self.__dict__.copy()
