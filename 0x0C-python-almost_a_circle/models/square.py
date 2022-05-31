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

    def update(self, *args, **kwargs):
        """assigns each arg to it's appropro attribute"""
        index = 0  # use this to keep track of index while moving through args
        if len(args) == 0:  # use kwargs only if args doesn't exist
            for key, value in kwargs.items():  # access key & value or kwargs
                # assign given values to appropriate attribute based on key
                if key == 'id':
                    self.id = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
                if key == 'size':
                    self.size = value
        for arg in args:  # begin moving through arg tuple
            if index == 0:
                self.id = arg  # arg is an int so it must be assigned to attr.
            if index == 1:  # dont use elif bc need to check each index
                self.size = arg
            if index == 2:
                self.x = arg
            if index == 3:
                self.y = arg
            index += 1  # increment each index to check for it's existence
