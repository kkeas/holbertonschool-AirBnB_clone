#!/usr/bin/python3
"""stores instances into JSON"""
import json
import os.path
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """FILE STORAGE CLASS"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dict __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the Jason :P file (path: __file_path)"""
        with open(self.__file_path, mode='w', encoding='utf-8') as obj:
            dct = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(dct, obj)

    def reload(self):
        """Deserializes jason into __objects"""
        try:
            with open(self.__file_path, encoding='utf-8') as obj:
                dict = json.load(obj)
                for key, value in dict.items():
                    obj = eval(value['__class__'])(**value)
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass
