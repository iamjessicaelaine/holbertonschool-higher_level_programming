#!/usr/bin/python3
"""module creates an object from a 'JSON file'"""


import json


def load_from_json_file(filename):
    """creates an object from filename, a json file"""
    with open(filename, 'r', encoding="utf-8") as j:
        obj = json.load(j)
