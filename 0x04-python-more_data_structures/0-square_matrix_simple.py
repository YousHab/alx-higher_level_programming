#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for subList in matrix:
        List = [elt ** 2 for elt in subList]
        new_matrix.append(List)
    return new_matrix
