#!/usr/bin/python3
"""module defines the class square, child of rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """a model of a rectangle whse inherited from its parent Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = size
        self.__x = x
        self.__y = y

    def __str__(self):
        """overiding str method for square class"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.__x,
                                                         self.__y, self.__size)

    @property  # getter for size
    def size(self):
        return self.__size

    @size.setter  # setter for size
    def size(self, value):
        self.w_h_validate("width", value)
        self.__size = value
