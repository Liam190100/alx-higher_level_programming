#!/usr/bin/python3
"""This module defines a class of Square"""


class Square:
    """This class represents a square size"""

    def __init__(self, size=0):
        """Instantializes square by its size"""
        self.size = size  

    @property
    def size(self):
        """Returns the size of the specified square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size of square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of that square"""
        return self.__size ** 2
