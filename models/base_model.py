#!/usr/bin/python3
"""module base model"""

from uuid import uuid4
from datetime import datetime
import uuid
import models


class BaseModel:
    """class base model that defines attributes"""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        models.storage.new(self)

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                    f = '%Y-%m-%dT%H:%M:%S.%f'
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.strptime(value, f))

    def __str__(self):
        """returns string of an instance"""
        bname = self.__class__.__name__
        return f"[{bname}] ({self.id}) {self.__dict__}"

    def save(self):
        """c"""
        self.updated_at = datetime.now()
        models.storage.save()

    def test_dic(self):
        bm1 = BaseModel()
        dicc = bm1.to_dict()
        self.assertIsInstance(dicc, dict)
        self.assertIsInstance(dicc["updated_at"], str)
        self.assertIsInstance(dicc["created_at"], str)

    def to_dict(self):
        """returns key values"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
