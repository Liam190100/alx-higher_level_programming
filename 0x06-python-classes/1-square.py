#!/usr/bin/python3
"""A class Square with a private instance attribute Size"""

class Square:
    """This class represents a square with a private size attribute."""

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square's sides.

        Attributes:
            __size (int): The private instance attribute storing the square's size.
        """
        self.__size = size

