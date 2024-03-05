#!/usr/bin/python3
""" Pascal Triangle """


def pascal_triangle(n):
    """ Pascal triangle """
    big_list = []
    for i in range(n):
        list = []
        for j in range(i + 1):
            if (j == 0) or (j == i):
                list.append(1)
            else:
                list.append(big_list[i - 1][j - 1] + big_list[i - 1][j])
        big_list.append(list)

    return big_list
