#!/usr/bin/python3
"""
Module 8-rectangle
"""


class Rectangle:
    """Class Rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Init a Rectangle.

        Args:
            width: width of the rectangle (int)
            height: height of the rectangle (int)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += str(self.print_symbol)
            rec_str += '\n'
        return rec_str[:-1]

    def __repr__(self):
        
        return "Rectangle({}, {})".format(self.__width, self.__height)
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rectangle_1 Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rectangle_2 Rectangle")
        if rectangle_1.area() == rectangle_2.area() or rectangle_1.area() > rectangle_2.area():
            return rect_1
        if rectangle_1.area() < rectangle_2.area():
            return rectangle_2
    def perimeter(self):

         if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

     def __del__(self):

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
