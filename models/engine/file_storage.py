#!/usr/bin/python3
'''file storage module'''

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """ FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        public instance method to return FileStorage
        objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        public instance method that sets __objects
        with obj with key <obj class name> id
        """
        if obj:
            key = "{}.{}".format(obj.__class__.name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes objects to the JSON path
        """
        inst_dict = dict()
        for key, value in FileStorage.__objects.items():
            inst_dict[key] = value.to_dict().copy()
        with open(FileStorage.__file_path, mode='w') as my_file:
            json.dump(inst_dict, my_file)

    def reload(self):
        """
        public instance method that serializes
        a JSON file to __objects.
        """
        try:
            with open(FileStorage.__file_path, mode='r') as my_file:
                inst_dict = json.load(my_file)

            for key, value in inst_dict.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
