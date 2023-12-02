#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    n = len(matrix) - 1
    for i in range(0, n):
        m = len(matrix[i]) - 1
        for j in range(0, m):
            if j == m:
                print("{}".format(matrix[i][j]), end="$\n")
            else:
                print("{}".format(matrix[i][j]), end=" ")
