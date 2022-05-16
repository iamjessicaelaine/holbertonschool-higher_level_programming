#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for number in range(0, len(row)):
            print("{:d}".format(row[number]), end=' ')
        print("".format('\n'))
