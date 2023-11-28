#!/usr/bin/python3
""" 0-pascal_triangle.py """


def pascal_triangle(n):
    """ returns a list of lists of integers representing
    the Pascal’s triangle of n """
    if n <= 0:
        return []
    else:
        BigArr = []
        for i in range(n):
            smallArray = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    smallArray.append(1)
                else:
                    smallArray.append(BigArr[i - 1][j - 1] + BigArr[i - 1][j])
            BigArr.append(smallArray)

        return BigArr
