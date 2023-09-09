#!/usr/bin/python3
"""
Module 6-rectangle
"""


class Rectangle:
    """
    Class Rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Init Rectangle.

        Args:
            width: width of the rectangle (int)
            height: height of the rectangle (int)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __repr__(self):

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):

        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width is integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height is integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for x in range(self.__height):
            for y in range(self.__width):
                rectangle_str += '#'
            rectangle_str += '\n'
        return rectangle_str[:-1]

    def area(self):

        return self.__width * self.__height

    def perimeter(self):

        if self.__height == 0 or self.__width == 0:
            return 0

        return 2 * (self.__width + self.__height)
