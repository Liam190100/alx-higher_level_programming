#!/usr/bin/python3
"""
This module defines a Square class that represents a square shape.

The Square class has methods to set and retrieve the size of the square,
calculate the area, and print a visual representation of the square using '#'.
"""

class Square:
    """
    Represents a square with a size attribute and related methods.
    
    Attributes:
        size (int): The size of the square's sides.
    """

	def __init__(self, size=0):
        """
        Initialize a new Square instance with a specified size.

        Args:
            size (int): The size of the square's sides. Default is 0.
        """
	self.size = size

	@property
	def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square's sides.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print a visual representation of the square using '#'.

        If the size is 0, an empty line is printed.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

