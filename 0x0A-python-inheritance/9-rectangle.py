#!/usr/bin/python3
"""write a class Rectangle that inherits from class BaseGeometry"""


class BaseGeometry:
    """defines a class BaseGeometry"""

    def area(self):
        """public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """class method which validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """birthing BaseGeometry's first child"""
    def __init__(self, width, height):
        """instantiating parent & child attributes & validating values"""
        # validate and define  width & height
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    # overriding parent's area method for child
    def area(self):
        """finds area of rectangle"""
        return (self.__height * self.__width)

    def __str__(self):
        """define what str() returns"""
        return("[Rectangle] {}/{}".format(self.__width, self.__height))

    def __repr__(self):
        """defines what print() will print"""
        print("[Rectangle] {}/{}".format(self.__width, self.__height))
