#!/usr/bin/python3
"""
Define a class of the Myint
"""


class MyInt(int):
    """
    A class that inverted equality and inequality operators.

    This class overrides equality (==) and inequality (!=) operators
    inverted behavior compared to regular int objects.

    Attributes:
        Inherits all attributes from the int class.

    Example:
        >>> a = MyInt(5)
        >>> b = MyInt(10)
        >>> a == b
        False  # Inverted behavior compared to regular int objects
        >>> a != b
        True   # Inverted behavior compared to regular int objects
    """

    def __eq__(self, other):
        """
        Override the equality operator (==) to invert its behavior.

        Args:
            other (int or MyInt): The value to compare with.

        Returns:
            bool: True if self is not equal to other, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality operator (!=) to invert its behavior.

        Args:
            other (int or MyInt): The value to compare with.

        Returns:
            bool: True if self is equal to other, False otherwise.
        """
        return super().__eq__(other)
