#!/usr/bin/python3

import json
import csv
import os.path


class Base:
    """Base class for objects"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the object with an optional ID"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dict):
        """Convert a list of dictionaries to a JSON string"""
        if list_dict is None:
            list_dict = []
        return json.dumps(list_dict)

    @staticmethod
    def from_json_string(json_str):
        """Convert a JSON string to a list of dictionaries"""
        if json_str is None or len(json_str) == 0:
            return []
        return json.loads(json_str)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a JSON file"""
        filename = cls.__name__ + ".json"
        obj_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                obj_dicts.append(obj.to_dictionary())
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(obj_dicts))

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with the given dictionary attributes"""
        if cls.__name__ == "Rectangle":
            new_obj = cls(10, 10)
        else:
            new_obj = cls(10)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """Load objects from a JSON file and create instances"""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as file:
            obj_dicts = cls.from_json_string(file.read())
        obj_instances = []
        for obj_dict in obj_dicts:
            obj_instances.append(cls.create(**obj_dict))
        return obj_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize objects to a CSV file"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize objects from a CSV file"""
        filename = cls.__name__ + ".csv"
        obj_list = []
        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for args in csv_reader:
                dictionary = {
                    "id": int(args[0]),
                    "width": int(args[1]),
                    "height": int(args[2]),
                    "x": int(args[3]),
                    "y": int(args[4]),
                }
                if cls.__name__ == "Rectangle":
                    if cls.__name__ == "Rectangle":
                        x = int(args[3])
                else:
                    x = int(args[2])
                obj = cls.create(**dictionary)
                obj_list.append(obj)
        return obj_list

