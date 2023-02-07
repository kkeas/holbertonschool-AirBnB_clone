#!/usr/bin/python3
import uuid 
import models
from datetime import datetime



class BaseModel:
    def __init__(self, *args, **kwargs):
        """ Initialize the BaseModel instance with id, created_at and updated_at """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if 'created_at' in kwargs:
                self.created_at = datetime.datetime.strptime(kwargs['created_at'],
                                                             '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                self.updated_at = datetime.datetime.strptime(kwargs['updated_at'],
                                                             '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ Prints a string representation of BaseModel instance """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the updated_at attribute with the current datetime """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Returns a dictionary representation of BaseModel instance """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
