#!/usr/bin/env python3
"""BaseModel Module"""

import models
import uuid
import datetime
import pytz


class BaseModel:
    """class defines common attributes and methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel class instances"""
        if kwargs is not None and len(kwargs) > 0:
            if "id" in kwargs.items():
                pass
            else:
                self.id = str(uuid.uuid4())
            if "created_at" in kwargs.items():
                pass
            else:
                self.created_at = datetime.datetime.now()
            if "upated_at" in kwargs.items():
                pass
            else:
                self.updated_at = datetime.datetime.now()
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at":
                        self.created_at = datetime.datetime.\
                                strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                        continue
                    elif key == "updated_at":
                        self.updated_at = datetime.datetime.\
                                strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                        continue
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """string representation of class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """Updates the attribute updated_at with current datetime"""
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns the diictionry of key/value of the instance"""
        attributes = {"id": self.id, "created_at": self.created_at.isoformat(),
                      "updated_at": self.updated_at.isoformat()}
        new_dict = self.__dict__.copy()
        for attr in attributes:
            if attr in new_dict:
                new_dict[attr] = attributes[attr]
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
