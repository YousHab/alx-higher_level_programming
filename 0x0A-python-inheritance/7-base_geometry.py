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

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

bg = BaseGeometry()

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))