#!/usr/bin/python3
"""
Module of the JSON
"""
import json


def to_json_string(my_obj):
    """ Function that returns JSON object

    Returns:
        my_obj:JSON object 

    """
    return json.dumps(my_obj)
