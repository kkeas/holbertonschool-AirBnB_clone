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
        objects_dict = {}
        for key, value in FileStorage.__objects.items():
            objects_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(objects_dict, f)

    def reload(self):
        """ Deserialize __objects from JSON file """
        dct = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review
        }

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as fd:
                obj_dict = json.load(fd)
                for key, value in obj_dict.items():
                    self.new(dct[value['__class__']](**value))
            return
