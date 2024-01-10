#!/usr/bin/python3

"""
====
Module withe the class BaseGeometry
====
"""


class BaseGeometry():
    """ BaseGeometry class
    """

    @classmethod
    def area(self):
        """ Raises an Exception with the message area() is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Instance method that validates value
        """

        if not isinstance(value, int):
            raise TypeError("name must be an integer")

        if value == 0:
            raise ValueError("age must be greater than 0")
