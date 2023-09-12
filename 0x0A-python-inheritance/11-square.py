#!/usr/bin/python3
"""Class Square that inherits Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Class square"""

    def __init__(self, size):
        """Initializes a square with size"""
        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def area(self):
        """Return area of square"""
        return self.__size ** 2

    def __str__(self):
        """Return square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
