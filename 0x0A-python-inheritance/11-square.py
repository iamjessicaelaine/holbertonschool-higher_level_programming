#!/usr/bin/python3
"""write a class square that inherits from rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines square class, child to Rectangle"""
    def __init__(self, size):
        """instantiating attibutes & validating size"""
        self.integer_validator("size", size)
        self.__size = size
        self.__height = size
        self.__width = size

    def area(self):
        """find the area of square"""
        return (self.__size ** 2)

    def __str__(self):
        """define what str() returns for square"""
        return("[Square] {}/{}".format(self.__width, self.__height))

    def __repr__(self):
        """define what print() prints for square"""
        return("[Square] {}/{}".format(self.__width, self.__height))
