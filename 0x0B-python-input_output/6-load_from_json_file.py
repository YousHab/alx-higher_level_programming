#!/usr/bin/python3

"""
Module with the function load_from_json_file.
"""


import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a “JSON file”.

    Args:
        filename: the file's name.

    """
    with open(filename, "r", encoding="utf-8") as my_file:
        my_obj = json.load(my_file)
        return my_obj
