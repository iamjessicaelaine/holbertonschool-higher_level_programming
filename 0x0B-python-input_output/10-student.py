#!/usr/bin/python3
"""module defines Student class"""


class Student:
    """class which contains student data & method to retrieve attributes"""
    def __init__(self, first_name, last_name, age):
        """student's instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """get a dict representation of Student instance w/ filter option"""
        if attrs is None or type(attrs) is not list:
            dictrep = vars(self)
            return dictrep
        filterdict = {}
        for key, value in dictrep.items():
            if key in attrs:
                filteredict[key] = value
        return filterdict
