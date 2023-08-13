#!/usr/bin/python3
"""
    module for creating file storage
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """
        class FileStorage
        private class attributes:
            __file_path(str): the path to the some file
            __objects(dict): this will store all objects
    """
    __file_path = 'file.json'
    __objects = {}
    classes = {"BaseModel": BaseModel,
               "State": State,
               "City": City,
               "Amenity": Amenity,
               "Place": Place,
               "Review": Review,
               "User": User}


    def all(self):
        """
            returns the directory __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
            sets in __objects the obj
        """
        key = obj.__class__.__name__ + '.' + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
            serializes __objects to the JSON the file
        """
        my_dict = {}
        for k, v in self.__objects.items():
            my_dict[k] = v.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='UTF-8') as f:
            json.dump(my_dict, f)

    def reload(self):
        """
            deserializes the JSON file to the __objects
        """
        try:
            with open(FileStorage.__file_path, mode="r") as f:
                new_dict = json.load(f)
                for k, v in new_dict.items():
                    base = FileStorage.classes[v["__class__"]](**v)
                    FileStorage.__objects[k] = base
        except FileNotFoundError:
            pass
