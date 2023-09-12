#!/usr/bin/python3
"""
Module that writes to a utf-8 file
"""


def write_file(filename="", text=""):
    """Writes a utf-8 file

    Args:
        filename: name of the file
        text: text to write

    Returns
        Number of chars: num_chars

    """

    with open(filename, 'w', encoding="utf-8") as file:
        num_chars = file.write(text)
        return num_chars
