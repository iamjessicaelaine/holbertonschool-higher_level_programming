#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for elem in a_dictionary:
        if elem == key:
            del a_dictionary[elem]
            return a_dictionary
