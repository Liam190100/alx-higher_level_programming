#!/usr/bin/python3
"""
This Module contains one function
"""


def lookup(obj):
    """Returns list of available
    attributes and methods of an object:
    """
    return [attribute for attribute in dir(obj)]
