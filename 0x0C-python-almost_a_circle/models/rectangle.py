#!/usr/bin/python3
"""module defines the rectangle that inherits from Base"""


class Base:
    """the base class, super class, parent class, 1 ring to rule them all"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiation of base w/ id attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def w_h_validate(self, name, value):
        """method to validate width & height"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def x_y_validate(self, name, value):
        """method to validate x & y"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))


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
