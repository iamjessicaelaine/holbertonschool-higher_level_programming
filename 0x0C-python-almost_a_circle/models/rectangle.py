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


class Rectangle(Base):
    """a model of a rectangle who has inherited from it's parent Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiation of child rectangle aka class constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property  # decorator to set width's getter
    def width(self):  # method used to get width
        return self.__width

    @width.setter  # decorator to width's setter
    def width(self, value):  # method to change value of width
        self.__width = value

    @property  # decorator to set height's getter
    def height(self):  # method to get height
        return self.__height

    @height.setter  # decorator set height's setter
    def height(self, value):  # method to change value of height
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self,  value):
        self.__y = value
