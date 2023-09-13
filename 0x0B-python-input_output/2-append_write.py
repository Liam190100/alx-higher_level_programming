#!/usr/bin/python3
"""
Module appends to a text file
"""


def append_write(filename="", text=""):
    """ Function that appends to a utf-8 file and if it doesn't
    exitst it is created
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
