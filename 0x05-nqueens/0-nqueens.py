#!/usr/bin/python3
""" queens problem """

import sys

if (len(sys.argv) != 2):
    print('Usage: nqueens N')
    exit(1)

try:
    int_value = int(sys.argv[1])
    if (int_value < 4):
        print('N must be at least 4')
        exit(1)
except Exception:
    print('N must be a number')
    exit(1)


def add_reserved_pairs(x: int, y: int, upper: int,
                       reserved_pairs) -> None:
    """ Add diagonal pairs """
    xx = x - 1
    yy = y - 1

    while xx >= 0 and yy >= 0:
        reserved_pairs.add((xx, yy))
        xx -= 1
        yy -= 1

    xx = x - 1
    yy = y + 1

    while xx >= 0 and yy < upper:
        reserved_pairs.add((xx, yy))
        xx -= 1
        yy += 1

    xx = x + 1
    yy = y - 1

    while xx < upper and yy >= 0:
        reserved_pairs.add((xx, yy))
        xx += 1
        yy -= 1

    xx = x + 1
    yy = y + 1

    while xx < upper and yy < upper:
        reserved_pairs.add((xx, yy))
        xx += 1
        yy += 1


def get_available_columns(x: int, upper: int, reserved_columns,
                          reserved_pairs):
    """ Get available columns """
    possible_values = set()
    for i in range(upper):
        if i not in reserved_columns:
            possible_values.add(i)
    for xx, yy in reserved_pairs:
        if (xx == x and yy in possible_values):
            possible_values.remove(yy)
    return possible_values


def get_possible_solutions(x: int, y: int, upper: int,
                           reserved_rows,
                           reserved_columns,
                           reserved_pairs):
    """ Get all possible solutions """
    reserved_columns.append(y)
    reserved_rows.append(x)
    add_reserved_pairs(x, y, upper, reserved_pairs)

    values = get_available_columns(x + 1, upper, reserved_columns,
                                   reserved_pairs)

    if (len(values) == 0):
        if (len(reserved_columns) == upper):
            solution = []
            counter = 0
            for column in reserved_columns:
                solution.append([counter, column])
                counter += 1
            print(solution)
        return

    for yy in values:
        get_possible_solutions(x + 1, yy, upper, list(reserved_rows),
                               list(reserved_columns), set(reserved_pairs))


def get_queens(number: int) -> None:
    """ Main function to get the queens solutions """
    for i in range(number):
        reserved_rows = []
        reserved_columns = []
        reserved_pairs = set()
        get_possible_solutions(0, i, number, reserved_rows,
                               reserved_columns, reserved_pairs)


get_queens(int_value)
