#!/usr/bin/python3
""" Module for base model """


import uuid
from datetime import datetime


class BaseModel():
    """ Base class that other objects will inherit from. """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """returns a a string containing class name, id and class atrributes """
        return '[{}] <{}> {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates updated_to with current datetime """
        self.created_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary representation of an instance"""
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.__dict__['created_at'].isoformat()
        new_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        return (new_dict)
