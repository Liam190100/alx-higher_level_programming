#!/usr/bin/python3
"""
This module defines a class Square with a private instance
attribute size
"""


class Square:
    """
    This class represents a class square with a size"""

    def __init__(self, size=0):
        """This square with the given size"""
        self.size = size

    @property
    def size(self):
        """This method returns the size square"""
        return self.__size

    @size.setter
    def size(self, value):
        """This method sets the size square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This method returns the square"""
        return self.__size ** 2

    def my_print(self):
        """This method prints the square # in stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
