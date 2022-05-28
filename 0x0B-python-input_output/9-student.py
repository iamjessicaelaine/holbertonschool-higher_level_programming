#!/usr/bin/python3
"""module defines Student class"""


class Student:
    """class which contains student data & method to retrieve attributes"""
    def __init__(self, first_name, last_name, age):
        """student's instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dict representation of Student instance"""
        dictrep = vars(self)
        return dictrep
