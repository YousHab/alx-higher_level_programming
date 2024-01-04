#!/usr/bin/python3
""" RECTANGLE TASK1
"""


class Rectangle:
    """ A class representing a rectangle
    """
    def __init__(self, width=0, height=0):
        """ attribute assigment here engages setters defined below

        Attributes:
            width: the horizontal dimension of rectangle
            height: the vertical dimension of rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width getter.

        Returns:
            __width (int): horizontal dimension of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ The width setter.

        Args:
            value (int): the width

        Attributes:
            __width (int): horizontal dimension of the rectangle.

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ width getter.

        Returns:
            __width (int): horizontal dimension of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ The height setter.

        Args:
            value (int): the height value

        Attributes:
            __height (int): vertical dimension of the rectangle.

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
