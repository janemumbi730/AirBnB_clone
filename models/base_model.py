#!/usr/bin/python3
"""
Create class BaseModel
"""
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
        class BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
            initializes all instances of BaseModel
        """
        if kwargs:
            self.updated_at = datetime.\
                strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            self.created_at = datetime.\
                strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            for k, v in kwargs.items():
                if k not in ['updated_at', 'created_at', '__class__']:
                    self.__setattr__(k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
            prints a string representation 
        """
        return '[{}] ({}) {}'\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
            updates the public instance attribute
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
            returns dictionary of key values of instance
        """
        dict = self.__dict__.copy()
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        dict['__class__'] = self.__class__.__name__
        return dict
