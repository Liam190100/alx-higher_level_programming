#!/usr/bin/python3
"""
Module class BaseGeometry
"""


class BaseGeometry:
    """Class for geometry objects"""

    def area(self):
        """Raises an exception with the message area() if not successful"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Assume name is always a string"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
