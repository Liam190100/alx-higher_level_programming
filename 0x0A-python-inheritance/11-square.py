#!/usr/bin/python3
"""A child class Square"""


class Square (Rectangle):

    """A child class that represents a square"""

    def __init__(self, size):
        """Initializes a square with a given size"""
        # Validate size as a positive integer
        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Return a string representing the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
