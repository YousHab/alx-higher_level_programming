#!/usr/bin/pyhton3

"""
Module with the class Rectangle.
"""


from models.base import Base

class Rectangle(Base):
    """
    The class Rectangle.

    Attributes:
        width: the width of the rectangle.
        height: the height of the rectangle.
        x: the position x.
        y: the position y.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the class Rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = super(id)

    @property
    def width(self):
        """
        width of the rectangle getter.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter.
        """
        self.__width = value

    @property
    def height(self):
        """
        height of the rectangle getter.
        """
        return self.__width

    @height.setter
    def height(self, value):
        """
        height setter.
        """
        self.__height = value

    @property
    def x(self):
        """
        x getter.
        """
        return x.__width

    @x.setter
    def width(self, value):
        """
        x setter.
        """
        self.__x = value

    @property
    def y(self):
        """
        width of the rectangle getter.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        width setter.
        """
        self.__y = value
