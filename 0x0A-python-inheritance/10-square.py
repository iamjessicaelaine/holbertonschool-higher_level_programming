#!/usr/bin/python3
"""writes a class Square, child to Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines rectangle's child class, square"""
    def __init__(self, size):
        "instantiating attributes & validating size"""
        self.integer_validator("size", size)
        self.__size = size
        # need to assign child class value to parent class atrributes
        self.__width = size
        self.__height = size

    def area(self):
        """find area of square"""
        return (self.__size ** 2)
