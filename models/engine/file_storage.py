#!/usr/bin/python3
"""FileStorage module"""

from models.base_model import BaseModel
import json

class FileStorage:
    """Serializes to JSON file and deserializes JSON file to instances

    Attributes:
        __file_path(str): path to JSON file
        __objects(dict): dictionary to store all objects

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary 
        Returns:
            __objects(dict): dictionary of objects
        """
        return self.__objects

    def new(self, obj):
        """Sets in dictionary the obj with key <obj class name>.id"""
        if obj is not None:
            name = type(obj).__name__ + '.' + obj.id
            self.__objects[name] = obj

    def save(self):
        """Serializes objects to the JSON file"""
        json_ob = {}
        for key, value in self.__objects.items():
            json_ob[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding = 'utf8') as json_file:
            json.dump(json_ob, json_file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as json_file:
                obj_dict = json.load(json_file)
            for key, value in obj_dict.items():
                self.__objects[key] = BaseModel(**value)
        except:
            pass
                

