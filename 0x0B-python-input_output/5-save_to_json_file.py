#!/usr/bin/python3
"""module writes an object to a text file using a json representation"""


import json


def save_to_json_file(my_obj, filename):
    """function writes my_obj to filename using a JSON representation"""
    with open(filename, 'w', encoding="utf-8") as j:
        json.dump(my_obj, j)
