#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix.copy()

    for a in range(len(matrix)):
        new[a] = list(map(lambda x: x**2, matrix[a]))

    return (new)
