#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # create an empty matrix
    newmatrix = [[0 for x in range(len(matrix))
                    for i in range(len(matrix[0]))]]
    # 1st loop access rows, 2nd loop the columns
    for x in range(len(matrix)):
        for i in range(len(matrix[0])):
            newmatrix[x][i] = matrix[x][i] ** 2
    return newmatrix
