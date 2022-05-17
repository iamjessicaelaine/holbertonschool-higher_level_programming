#!/usr/bin/python3
"""writes a class Rectangle"""


class Rectangle:
    """an attempt to model a rectangle"""
    def __init__(self, width=0, height=0):  # instantiation w/ optional w & h
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width  # create private instance attribute
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height  # create private instance attribute

    @property
    def width(self):  # method used to get width
        return self.__width

    @width.setter
    def width(self, value):  # method used to change width value
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):  # method used to retrieve height attributer
        return self.__height

    @height.setter
    def height(self, value):  # method used to change height value
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):  # public instance method returns rectangle area
        return (self.__height * self.__width)

    def perimeter(self):  # public instance method returns permiter
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width + self.__height) * 2)
