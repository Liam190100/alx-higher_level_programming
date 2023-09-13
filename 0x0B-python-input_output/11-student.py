#!/usr/bin/python3

"""
Module 10-student a class defining a Student
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Student in JSON format
        """
        if (attrs is None):
            return self.__dict__
        return dict(filter(lambda c: c[0] in attrs, self.__dict__.items()))

    def reload_from_json(self, json):
        """
        Load data from json into object

        """
        for c, d in json.items():
            self.__dict__[c] = d
