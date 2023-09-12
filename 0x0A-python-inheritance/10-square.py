#!/usr/bin/python3
"""Define class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Child class square
    """

    def __init__(self, size):
        """
        Init square size
        """
        self.integer_validator("size", size)

        self.__size = size

        super().__init__(size, size)

    def area(self):
        """Return square"""
        return self.__size ** 2
