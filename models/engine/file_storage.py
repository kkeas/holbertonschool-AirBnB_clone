#!/usr/bin/python3
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

class FileStorage:
    """serializes instances to a JSON file"""
    __file_path = "file.json"
    # dictionary to store all objects
    __objects = {}

    def all(self):
        """returns _objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets _objects w/obj to key obj class name"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes _obj to the JSON file path"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """deserializes the JSON file to __obj"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass
