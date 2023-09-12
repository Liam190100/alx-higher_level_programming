#!/usr/bin/python3
""" Module that creates class Student
"""


class Student:
    """Public Class to create student """

    def __init__(self, first_name, last_name, age):
        """ initialize the self"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns directory"""
        return self.__dict__.copy()
