#!/usr/bin/python3
"""the class that is the base of all other classes"""


class Base:
    """base class to manage id attribute in all future classes"""
    __nb_objects = 0  # this is a class attribute & a static member of class

    def __init__(self, id=None):
        """instantiation of base w/ id attribute"""
        if id is not None:
            self.id = id
        else:
            # give self.id a unique __nb_objects in each instance
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
    
    def area(self):
        """public instance method to be inherited by future kids"""
        raise Exception("area() is not implemented")
