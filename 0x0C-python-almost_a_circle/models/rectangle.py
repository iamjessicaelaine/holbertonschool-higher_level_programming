#!/usr/bin/python3
"""module defines the rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """a model of a rectangle who has inherited from it's parent Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiation of child rectangle aka class constructor"""
        super().__init__(id)
        self.w_h_validate("width", width)
        self.__width = width
        self.w_h_validate("height", height)
        self.__height = height
        self.x_y_validate("x", x)
        self.__x = x
        self.x_y_validate("y", y)
        self.__y = y

    @property  # decorator to set width's getter
    def width(self):  # method used to get width
        return self.__width

    @width.setter  # decorator to width's setter
    def width(self, value):  # method to change value of width
        self.w_h_validate("width", value)
        self.__width = value

    @property  # decorator to set height's getter
    def height(self):  # method to get height
        return self.__height

    @height.setter  # decorator set height's setter
    def height(self, value):  # method to change value of height
        self.w_h_validate("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.x_y_validate("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self,  value):
        self.x_y_validate("y", value)
        self.__y = value

    def area(self):
        """method finds & returns area of rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """prints Rectangle instance w/ #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectprint = ""
            for yfactor in range(self.__y):
                rectprint += "\n"
            for col in range(self.__height):
                for xfactor in range(self.__x):
                    rectprint += " "
                for row in range(self.__width):
                    rectprint += "#"
                if col != self.__height - 1:
                    rectprint += "\n"
            print(rectprint)

    def __str__(self):
        """overriding __str__ method for rectangle class"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    def update(self, *args, **kwargs):
        """assigns each arg to it's appropro attribute"""
        index = 0  # use this to keep track of index while moving through args
        if len(args) == 0:  # use kwargs only if args doesn't exist
            for key, value in kwargs.items():  # access key & value or kwargs
                # assign given values to appropriate attribute based on key
                if key == 'id':
                    self.id = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
        for arg in args:  # begin moving through arg tuple
            if index == 0:
                self.id = arg  # arg is an int so it must be assigned to attr.
            if index == 1:  # dont use elif bc need to check each index
                self.__width = arg
            if index == 2:
                self.__height = arg
            if index == 3:
                self.__x = arg
            if index == 4:
                self.__y = arg
            index += 1  # increment each index to check for it's existence

    def to_dictionary(self):
        """turn rectangle's attributes into a dictionary"""
        return vars(Rectangle)
