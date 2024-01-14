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
        return "[Square] ({}) {}/{} - {} - in our case, width or height".format(
            self.id, self.__x, self.__y, self.__width)

    def update(self, *args, **kwargs):
        """
        
        """
        if args:
            pass
        
        elif kwargs:
            pass
        
