#!/usr/bin/python3
""" Module for base model """

import uuid
from datetime import datetime


class BaseModel():
    """ base model class """
    def __init__(self, *args, **kwargs):
        """ class constructor for base model """
        if kwargs:
            kwargs['created_at'] = datetime.strftime('%Y-%m-%d %H:%M:%S')
            kwargs['updated_at'] = datetime.strftime('%Y-%m-%d %H:%M:%S')

            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """returns a string """
        return '[{}] ({}) {}'.format(self.__class__.__name__,
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
