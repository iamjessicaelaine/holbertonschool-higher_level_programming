#!/usr/bin/python3
"""module defines the class square, child of rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """a model of a rectangle whse inherited from its parent Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width, height, x, y, id)
        self.__height = size
        self.__width = size

    def __str__(self):
        """overiding str method for square class"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.__x,
                                                         self.__y, self.__width)

    @property  # getter for size
    def size(self):
        return self.__size

    @size.setter  # setter for size
    def size(self, value):
        self.w_h_validate("width", value)
        self.__width = value
        self.__height = value
