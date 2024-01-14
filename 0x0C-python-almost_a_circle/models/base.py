#!/usr/bin/python3

"""
Module with the class Base
"""


import json


class Base:
    """
    Base class

    Attributes:
        id: an identifier for instances of the class.
        n_object (int): A class attribute to keep track of the
        number of objects created.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the class Base.

        Parameters:
            id (id, optional): An optional identifier.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method that creates a JSON string from a list of dictionaries.

        Args:
            list_dictionaries: a list of dictionaries to be transformed.

        Returns:
            JSON string representation of list_dictionaries.
        """
        json_string = ""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
