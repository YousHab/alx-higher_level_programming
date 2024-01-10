#!/usr/bin/python3

"""
===================================
module with classes BaseGeometry and Rectangle
===================================
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """method for calculated area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method for validate if a num is integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Calculate the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """__str__ method for return the next stringù
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """ The class square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculate the area of a square
        """
        return self.__size ** 2
    
    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
