#!/usr/bin/python3

def matrix_divided(matrix, div):
    """ function that divides all elements of a matrix

    Args:
        matrix: the matrix to be divided
        div: div

    Raises:
        TypeError: if the elements are not integers or floats
        TypeError: if the rows have diferrent lengths
        TypeError: if div is not a number
        ZeroDivisionError: if div = 0

    Returns a new matrix
    """
    err_message = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = matrix
    len_matrix = len(matrix)
    size_row = len(matrix[0])

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    for element in matrix:
        if len(element) != size_row:
            raise TypeError("Each row of the matrix must have the same size")

    for i in range(len_matrix):
        for j in range(size_row):
            n = new_matrix[i][j]
            if type(n) not in (int, float):
                raise TypeError(err_message)
            else:
                n = round(n / div, 2)
                new_matrix[i][j] = n

    return (new_matrix)
