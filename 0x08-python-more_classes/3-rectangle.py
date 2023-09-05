#!/usr/bin/python3

"""Define a Rectangle class."""


class Rectangle:
    """Class represents a rectangle."""

    def __init__(self, width=0, height=0):

        """Init self a new Rectangle.
        Args:
        width: width of rectangle (int).
        height: height of rectangle (int).
        """

        self.width = width
        self.height = height

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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []
        for row in range(self.__height):
            for column in range(self.__width):
                rectangle.append("#")
            if row != self.__height - 1:
                rectangle.append("\n")
        return "".join(rectangle)
