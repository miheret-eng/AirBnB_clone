#!/usr/bin/python3
"""TestFileStorage Module"""

import models
import unittest
import json
from models.engine import file_storage
import os
from models.base_model import BaseModel
FileStorage = file_storage.FileStorage


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    def test_all_returns_dict(self):
        """Test that all returns the FileStorage.__objects attr"""
        storage = FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage._FileStorage__objects)

    def test_save(self):
        """Test that save properly saves objects to file.json"""
        storage = FileStorage()
        new_dict = {}
        instance = BaseModel()
        instance_key = instance.__class__.__name__ + "." + instance.id
        new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))

    def test_new(self):
        """test that new adds an object to the FileStorage.__objects attr"""
        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        instance = BaseModel()
        instance_key = instance.__class__.__name__ + "." + instance.id
        storage.new(instance)
        test_dict[instance_key] = instance
        self.assertEqual(test_dict, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = save
