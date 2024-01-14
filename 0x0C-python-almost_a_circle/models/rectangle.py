#!/usr/bin/python3

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
        super().__init__(id)

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
        self.validate_int_for_size("width", value)
        self.__width = value

    @property
    def height(self):
        """
        height of the rectangle getter.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter.
        """
        self.validate_int_for_size("height", value)
        self.__height = value

    @property
    def x(self):
        """
        x getter.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter.
        """
        self.validate_int_for_xy("x", value)
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
        Prameters:
            value: the y value
        """
        self.validate_int_for_xy("y", value)
        self.__y = value

    def validate_int_for_size(self, name, value):
        """
        Method that validate that values are integers.

        Args:
            name: the name of the attribute.
            value: the value to be checked.
    
        Raises:
            TypeError: if the value is not int.
            ValueError: if width or height are <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def validate_int_for_xy(self, name, value):
        """
        Method that validate values.

        Args:
            name: the name of the attribute.
            value: the value to be checked.
    
        Raises:
            TypeError: if the value is not int.
            ValueError: if x or y are < 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(name))
    
    def area(self):
        """
        Method thar calculate the area.
        Returns:
            returns the area.
        """
        return self.__height * self.__width

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character #
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        str method
        Returns:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} -{}/{}".format(self.id,
                                                      self.__x,
                                                      self.__y,
                                                      self.__width,
                                                      self.__height)
    
    def update(self, *args, **kwargs):
        """
        This method assigns an argument to each attribute.
        Args:
            *args: tuple of arguments to add.
            **kwargs: a dictionary where each represents an attribute
            to the instance.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
