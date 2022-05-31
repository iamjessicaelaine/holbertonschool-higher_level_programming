#!/usr/bin/python3
"""module defines the class square, child of rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """a model of a rectangle whse inherited from its parent Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overiding str method for square class"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    @property  # getter for size
    def size(self):
        return self.width

    @size.setter  # setter for size
    def size(self, value):
        self.w_h_validate("width", value)
        self.width = value
        self.height = value
