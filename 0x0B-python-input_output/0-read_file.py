#!/usr/bin/python3

"""
Module read_file
"""


def read_file(filename=""):
    """Read and write in the stdout

    Args:
        filename: name file that read
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
