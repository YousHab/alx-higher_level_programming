#!/usr/bin/python3

"""
Module with the function save_to_json_file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file
    using a JSON representation

    Args:
        my_obj: the object to write.
        filename: the file to write into.
    """
    with open(filename, "w", encoding="UTF-8") as my_file:
        json.dump(my_obj, my_file, ensure_ascii=False, indent=2)
