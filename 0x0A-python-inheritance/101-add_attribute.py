#!/usr/bin/python3
"""A class that create new attribute to an object
if it’s possible"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it’s possible.

    Args:
        obj (object): object to add the attribute to.
        name (str): name of the attribute to add.
        value (any): value of the attribute to add.

    Raises:
        TypeError: If the object can't add new attributes.
    """
    # Check if the object has a __dict__ attribute that
    # allows adding new attributes
    if hasattr(obj, "__dict__"):
        # Set the new attribute with the given name and value
        setattr(obj, name, value)
    else:
        # Raise a TypeError exception if not successful
        raise TypeError("can't add new attribute")
