#!/usr/bin/python3
"""
Define class Square
"""


from __import__('9-rectangle') import Rectangle

class Square(Rectangle):

    """A child class square"""

    def __init__(self, size):
        """Initializes a square with a given size"""
        # Validate size
        self.integer_validator("size", size)

        self.__size = size

        super().__init__(size, size)

    def area(self):
        """Return the area square"""
        return self.__size ** 2

    def __str__(self):
        """Return a string square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
