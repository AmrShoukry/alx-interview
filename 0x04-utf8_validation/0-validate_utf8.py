#!/usr/bin/python3
""" UTF 8 validation """


def validUTF8(data):
    """ valid utf 8 function """
    for number in data:
        if (number < 128):
            continue
        if number >> 6 == 0b10:
            continue
        if number >> 5 == 0b110:
            continue
        if number >> 4 == 0b1110:
            continue
        if number >> 3 == 0b11110:
            continue
        return False
    return True
