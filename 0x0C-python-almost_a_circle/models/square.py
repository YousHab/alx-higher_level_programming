#!/usr/bin/python3

"""
Module with class Square that inherits from the
the class Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The class Square that inherits from Rectangle.
    Attributes:
        size: the size of the square.
        x: the x position.
        y: the y position.
    """
    def __inti__(self, size, x=0, y=0, id=None):
        """
        Constructor of the class Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the property "size".
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for "size".
        """
        super().validate_int_for_size("width", value)
        self.__width = value
        self.__height = value

    def __str__(self):
        """
        Override the __str__ method.
        Returns a formatted string: [Square] (<id>) <x>/<y> - <size>
        """
        s1 = "[Square] ({}) {}/{} - {} - in our case, width or height".format(
            self.id, self.__x, self.__y, self.__width)
        return s1

    def update(self, *args, **kwargs):
        """
        Updates Square properties.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__size = args[1]
            if len(args) >= 3:
                self.__x = args[2]
            if len(args) >= 4:
                self.__y = args[3]

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Method that returns the dictionary representation
        of a Square.
        """
        dictionary_keys = ["id", "size", "x", "y"]
        dictionary_values = [self.id,
                             self.__size,
                             self.__x,
                             self.__y]
        return dict(zip(dictionary_keys, dictionary_values))
