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
        BG.integer_validator("width", width)
        self.__width = width
        BG.integer_validator("height", height)
        self.__height = height
