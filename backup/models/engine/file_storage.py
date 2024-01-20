#!/usr/bin/python3
import json


class FileStorage:
    """
    A class to handle serialization and deserialization of json format data
    """

    __file_path = "data.json"
    __objects = {}


    def all(self):
        """
        Returns the object dictionary, a dictionary of all created objects
        """
        return FileStorage.__objects


    def new(self, obj):
        """Adds a new object to the __object dictionary"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = str(obj)


    def save(obj):
        """Serializes the __objets dictionary into the json file"""
        try:
            with open(file=FileStorage.__file_path, mode="r") as json_file:
                saved_data = json.load(json_file)
        except FileNotFoundError:
            with open(file=FileStorage.__file_path, mode="w") as json_file:
                json.dump(FileStorage.__objects, json_file, indent=4)
        else:
            saved_data.update(FileStorage.__objects)
            with open(file=FileStorage.__file_path, mode="w") as json_file:
                json.dump(saved_data, json_file, indent=4)
    def reload(self):
        """Deserializes the JSON file to __objects dictionary"""
        try:
            with open(file=FileStorage.__file_path, mode="r") as json_file:
                FileStorage.__objects = json.load(json_file)
        except FileNotFoundError:
            pass
