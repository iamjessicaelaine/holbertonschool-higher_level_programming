#!/usr/bin/python3
"""module to return an object represented by a JSON string"""


import json


def from_json_string(my_str):
    """returns an object from my_str, a json string"""
    obj = json.loads(my_str)
    return obj
