#!/usr/bin/python3
"""
Module of the inherits
"""


def inherits_from(obj, a_class):
    """
    Function checks for instance and subclass
    """
    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    return False
