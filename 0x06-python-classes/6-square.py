#!/usr/bin/python3
"""
This module defines a class Square
"""


class Square:
    """
    This class represents a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """This method square size position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """This method returns size square"""
        return self.__size

    @size.setter
    def size(self, value):
        """This method sets square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """This method returns square"""
        return self.__position

    @position.setter
    def position(self, value):
        """This method sets square"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This method returns square"""
        return self.__size ** 2

    def my_print(self):
        """This method prints error in the stdout of the square #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
