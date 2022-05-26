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
            for row in range(self.__height):
                for col in range(self.__width):
                    rectprint += "#"
                if row != self.__height - 1:
                    rectprint += "\n"
            print(rectprint)

    def __str__(self):
        """overriding __str__ method for rectangle class"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)
