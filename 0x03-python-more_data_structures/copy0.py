#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
<<<<<<< HEAD
    newmatrix = [[0 for x in range(len(matrix))]
                 for i in range(len(matrix[0]))]
=======
    # create an empty matrix
    newmatrix = [[0 for x in range(len(matrix))
                    for i in range(len(matrix[0]))]]
    # 1st loop access rows, 2nd loop the columns
>>>>>>> 389849fccec5c18251b4b9a719852b276e61e2a7
    for x in range(len(matrix)):
        for i in range(len(matrix[0])):
            newmatrix[x][i] = matrix[x][i] ** 2
    return newmatrix
