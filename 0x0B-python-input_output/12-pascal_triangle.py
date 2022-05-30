#!/usr/bin/python3
"""module with a function that creates a representation of pascal's triangle"""


def pascal_triangle(n):
    """returns a matrix of ints repping pascal's trriangle to the n'th row"""
    rownumber = n  # new variable for n to better read my code
    pascalslist = []  # empty list to store my sublists/each row
    # append sub-lists into empty list created above
    if rownumber <= 0:
        return pascalslist

    for i in range(rownumber):
        pascalslist.append([])
        # then insert 1 into each sublist for future numbers to follow behind
        pascalslist[i].append(1)
        # now we determine the value of #s inside triangle
        for j in range(1, i):  # starting @ second element in row do math
            pascalslist[i].append(pascalslist[i-1][j-1] + pascalslist[i-1][j])
        # append 1 to end of list
        if (n != 0):
            pascalslist[i].append(1)
    return pascalslist
