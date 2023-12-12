#!/usr/bin/python3
""" minoperations """

def minOperations(n: int) -> int:
    """ minoperations """
    if (n <= 1):
        return 0
    operations: int = 2
    current: int = 2
    increments: int = 1
    
    while (n != current):    
        if (n % current == 0):
            operations += 2
            current *= 2
            increments *= 2
        else:
            operations += 1
            current += increments

    return operations
