#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # create new empty dictionary
    newdict = dict()
    # traverse dictionary to do math on each item
    for item in a_dictionary:
        newdict[item] = a_dictionary[item] * 2
    return newdict
