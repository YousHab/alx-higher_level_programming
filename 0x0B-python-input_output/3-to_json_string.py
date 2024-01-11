#!/usr/bin/python3
import json
"""
Module with the fucntion to_json_string
"""


def to_json_string(my_obj):
    """
    function that returns the JSON representation of an object

    Args:
        my_obj: the object to be transformed

    Returns:
        the JSON representation of my_obj
    """
    my_data = json.dumps(my_obj)
    return my_data
