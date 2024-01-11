#!/usr/bin/python3

"""
Module with the function from_json_string
"""


import json


def from_json_string(my_str):
    """
    function that returns an object (Python data structure)
    represented by a JSON string.

    Args:
        my_str: the string to be transformed

    Returns:
        An object (Python data structure)
        represented by a JSON string
    """

    my_data = json.loads(my_str)
    return my_data
