#!/usr/bin/python3
"""
Module writes an Object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an object
    text file JSONand save it
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
