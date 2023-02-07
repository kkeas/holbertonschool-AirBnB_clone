#!/usr/bin/python3
import uuid 
import models
from datetime import datetime



class BaseModel:
    """ Represent a class BaseModel that defines
    all common attributes/methods for other classes """ 
    
    def __init__(self, *args, **kwargs):
        
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value, t)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, t)
                else:
                    setattr(self, key, value)
                    
    def __str__(self):
        """returns string class"""
        return "[{}] ({}) {}".format(
        type(self).__name__,
        self.id,
        self.__dict__
        )
    
    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):
        new_dict = self.__dict__.copy()
