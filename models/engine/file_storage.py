#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json
import models
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
    """The class serializes to JSON file and back to objects

    Attributes:
        __file_path(str): path to the json file
        __objects(dict): dictionary of all objects created

    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns  __objects"""
        if cls is not None:
            new_dict = {}
            for k, v in self.__objects.items():
                if cls == v.__class__ or cls == v.__class__.__name__:
                    new_dict[k] = v
            return new_dict
        return self.__objects

    def new(self, obj):
        """Sets in __objects obj using key <obj class name>.id"""

        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        json_objs = {}
        for key in self.__objects:
            json_objs[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objs, f)

    def reload(self):
        """Deserializes JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                js = json.load(f)
            for key in js:
                self.__objects[key] = classes[js[key]["__class__"]](**js[key])
        except:
            pass
