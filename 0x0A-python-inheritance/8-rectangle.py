#!/usr/bin/python3
"""
class Rectangle BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class of the rectangle"""

    def __init__(self, width, height):
        """
        Instanciate a rectangle with a width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
