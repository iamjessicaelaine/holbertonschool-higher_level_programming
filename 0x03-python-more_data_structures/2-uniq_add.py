#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqsum = 0
    # use set method to get list removing elem repeats
    for elem in set(my_list):
        uniqsum += elem
    return uniqsum
