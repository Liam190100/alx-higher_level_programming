#!/usr/bin/python3
"""Module for the Rectangle class"""


class Rectangle:
    """Defines a Rectangle class with width and height attributes.

    Attributes:
        number_of_instances (int): Number of Rectangle instances.
            Increments with every instantiation and decrements with every deletion.
        print_symbol (str): The symbol used for representing the Rectangle.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantiates a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns a string representation of a filled Rectangle."""
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            rec_str += str(self.print_symbol) * self.__width + '\n'
        return rec_str[:-1]

    def __repr__(self):
        """Returns a string representation of a Rectangle instance
        that can be used to recreate the instance using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes a Rectangle instance."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance.

        Args:
            value (int): The width value, must be a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance.

        Args:
            value (int): The height value, must be a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a Rectangle instance.

        Returns:
            int: The area of the rectangle, given by height * width.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a Rectangle instance.

        Returns:
            int: The perimeter of the rectangle, given by 2 * (height + width).
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Finds the bigger Rectangle based on the area.

        Args:
            rect_1 (Rectangle): A Rectangle instance.
            rect_2 (Rectangle): Another Rectangle instance different from rect_1.

        Returns:
            Rectangle: The instance with the biggest area,
                or rect_1 if both rectangles have the same area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

