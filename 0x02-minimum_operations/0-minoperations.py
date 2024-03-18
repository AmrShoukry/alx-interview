#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """ min operations """
    if (n <= 1):
        return 0
    operations = 0
    copy = 0
    value = 1
    while value != n:
        if n % value == 0:
            copy = value
            value *= 2
            operations += 2
        else:
            value += copy
            operations += 1
    return operations
