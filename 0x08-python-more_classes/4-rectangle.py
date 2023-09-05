#!/usr/bin/python3

"""Define a class Rectangle."""


class Rectangle:
    """Class rectangle."""

    def __init__(self, width=0, height=0):
        """Init Rectangle.
        Args:
            width: width of rectangle (int).
            height: height of rectangle (int).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return width of rectangle."""
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
        """Returns height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height is integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter Rectangle."""
        if self.width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Return str of rectangle # character
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for m in range(self.__height):
            [rectangle.append('#') for m in range(self.__width)]
            if m != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """repr self of Rectangle."""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)
