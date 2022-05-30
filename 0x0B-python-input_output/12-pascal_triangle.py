#!/usr/bin/python3
"""module with a function that creates a representation of pascal's triangle"""


def pascal_triangle(n):
    """returns a matrix of ints repping pascal's trriangle to the n'th row"""
    rownumber = n  # new variable for n to better read my code
    pascslist = []  # empty list to store my sublists/each row
    # append sub-lists into empty list created above
    if rownumber <= 0:
        return pascslist
    else:
        for i in range(rownumber):
            pascslist.append([])
            # then insert 1 into each sublist for future numbers to follow
            pascslist[i].append(1)
            # loop computes math of other numbers based on pascal's math
            for j in range(1, i):  # starting @ second element in row do math
                pascslist[i].append(pascslist[i-1][j-1] + pascslist[i-1][j])
            # append 1 to end of list
            pascslist[i].append(1)
        return pascslist
