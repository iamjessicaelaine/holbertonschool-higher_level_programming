#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for number in range(0, len(row)):
            print("{:d}".format(number), end=' ')
        print("".format('\n'))
