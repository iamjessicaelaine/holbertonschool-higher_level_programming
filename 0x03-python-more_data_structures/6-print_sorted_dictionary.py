#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # sorted() similar to sort() but works on any iterable
    for elem in sorted(a_dictionary):
        print("{}: {}".format(elem, a_dictionary[elem]))
