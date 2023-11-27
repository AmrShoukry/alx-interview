#!/usr/bin/python3
""" 0-pascal_triangle.py """


def pascal_triangle(n):
    """ returns a list of lists of integers representing
    the Pascal’s triangle of n """
    if n <= 0:
        return []
    else:
        BigArray = []
        for i in range(n):
            smallArray = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    smallArray.append(1)
                else:
                    smallArray.append(BigArray[i - 1][j - 1] + BigArray[i - 1][j])
            BigArray.append(smallArray)

        return BigArray                