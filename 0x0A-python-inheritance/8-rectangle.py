#!/usr/bin/python3
BG = __import__('7-base_geometry').BaseGeometry

"""
===================================
module with class Rectangle
===================================
"""


class Rectangle(BG):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
