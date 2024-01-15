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
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs.

        Args:
            list_objs: a list of instances who inherits of Base.

        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding="utf-8") as my_file:
            my_file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.

        Args:
            json_string: a string representing a list of dictionaries

        Returns:
            empty list: if json_string is None or empty.
            list represented by json_string: otherwise.
        """
        if not json_string or len(json_string) == 0:
            my_list = []
        else:
            my_list = json.loads(json_string)
        return my_list

    @classmethod
    def create(cls, **dictionary):
        """ Loads instance frome dictionary
        Args:
            dictionary: a dictionary with the instance information.

        Returns:
            An instance with all attributes already set
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            instance = Rectangle(1, 1)
        elif cls is Square:
            instance = Square(1)
        else:
            instance = None
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r", encoding="utf-8") as my_file:
                json_string = my_file.read()
                json_to_dictionaries = cls.from_json_string(json_string)
                return [cls.create(**d) for d in json_to_dictionaries]
        except FileNotFoundError:
            return []
