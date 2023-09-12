#!/usr/bin/python3
"""
Module that JSON string
returns an object (Python data structure)
"""
import json


def from_json_string(my_str):
    """ Function that JSON object is return

    Returns:
        my_str: json loads

    """
    return json.loads(my_str)
