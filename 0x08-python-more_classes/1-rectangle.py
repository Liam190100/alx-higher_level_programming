#!/usr/bin/python3
"""
Module 1-rectangle
Defines a rectangle and its sides
"""


class Rectangle:
    """Class that represent a rectangle
    """
    def __init__(self, width=0, height=0):
        """Init and the self of Rectangle

        Attributes:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter - width property."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of the width

        Args:
            value: width of rectangle

        Raises:
            TypeError: if width not integer
            ValueError: if width is less 0 or 1
        """
        if (not isinstance(value, int)):
            raise TypeError("width is an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter - height property."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of the heigth

        Args:
            value: height of rectangle

        Raises:
            TypeError: if height not integer
            ValueError: if height is less 0 1
        """
        if (not isinstance(value, int)):
            raise TypeError("height is integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
