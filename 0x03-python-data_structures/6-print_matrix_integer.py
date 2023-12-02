#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    n = len(matrix) - 1
    for i in range(n + 1):
        m = len(matrix[i]) - 1
        for j in range(m + 1):
            if j == m:
                print("{}".format(matrix[i][j]))
            else:
                print("{}".format(matrix[i][j]), end=" ")
