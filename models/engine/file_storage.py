#!/usr/bin/python3

import json
from os.path import exists

class FileStorage:
    """FileStorage class."""
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        data = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    module = __import__("models." + class_name, fromlist=[class_name])
                    cls = getattr(module, class_name)
                    obj = cls(**value)
                    self.__objects[key] = obj

# Create a single instance of FileStorage
storage = FileStorage()
storage.reload()

