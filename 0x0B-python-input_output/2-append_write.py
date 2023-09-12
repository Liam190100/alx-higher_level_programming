#!/usr/bin/python3
"""
Fuction that write in the file
"""


def write_file(filename="", text=""):
     """ Function that appends to a utf-8 file and if it doesn't
    exitst it is created

    Args:
        filename: filename
        text: text to write

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
