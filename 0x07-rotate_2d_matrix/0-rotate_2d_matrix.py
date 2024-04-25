#!/usr/bin/python3
""" Rotate 2d Matrix """


def rotate_2d_matrix(matrix):
    """ Rotate 2d Matrix """
    n = len(matrix)
    rec(matrix, 0, n - 1)


def rec(matrix, start, end):
    """ Recursice calls """
    if end <= start:
        return

    for i in range(start, end):
        temp = matrix[start][i]

        matrix[start][i] = matrix[end - (i - start)][start]
        matrix[end - (i - start)][start] = matrix[end][end - (i - start)]
        matrix[end][end - (i - start)] = matrix[i][end]
        matrix[i][end] = temp

    rec(matrix, start + 1, end - 1)