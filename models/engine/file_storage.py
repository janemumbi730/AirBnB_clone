#!/usr/bin/python3

"""
makes file atorage
"""
from models.base_model import BaseModel
from models.review import Review
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
import json


class FileStorage:
    """
    the class file storege
    """
    __file_path = "file.json"
    __objects = {}
  
 def save(self):
        """
        JSON file objects
        """
        non_ser_dict = self.__objects
        ser_dict = {}

        for obj_id in non_ser_dict.keys():
            ser_dict[obj_id] = non_ser_dict[obj_id].to_dict()

        with open(self.__file_path, "w") as json_file:
            json.dump(ser_dict, json_file)
  
  def new(self, obj):
        """
        sets object
        """
        class_name = obj.__class__.__name__
        self.__objects[f"{class_name}.{obj.id}"] = obj

   
  def all(self):
        """
        returns dictionary
        """
        return self.__objects


  def reload(self):
        """
        JSON file to __objects
        """
        try:
            with open(self.__file_path) as json_file:
                ser_dict = json.load(json_file)
                for values in ser_dict.values():
                    cls_name = values["__class__"]
                    del values["__class__"]
                    self.new(eval(cls_name)(**values))

        except FileNotFoundError:
            return
