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
            return vars(self)
        filterdict = {}
        nofilter = vars(self)
        for key, value in nofilter.items():
            if key in attrs:
                filterdict[key] = value
        return filterdict

def reload_from_json(self, json):
    """replace all attributes with dictionary data"""
    nofilter = vars(self)
    nofilter.update(json)
