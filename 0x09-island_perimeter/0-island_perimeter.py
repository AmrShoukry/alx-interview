#!/usr/bin/python3
""" Island perimeter """


def island_perimeter(grid):
    """ get perimeter """
    counter = 0
    rows_count = len(grid)
    columns_count = len(grid[0])

    for i in range(rows_count):
        for j in range(columns_count):
            if grid[i][j] == 1:
                if i - 1 < 0 or grid[i - 1][j] == 0:
                    counter += 1
                if i + 1 >= rows_count or grid[i + 1][j] == 0:
                    counter += 1

                if j - 1 < 0 or grid[i][j - 1] == 0:
                    counter += 1
                if j + 1 >= columns_count or grid[i][j + 1] == 0:
                    counter += 1

    return counter
