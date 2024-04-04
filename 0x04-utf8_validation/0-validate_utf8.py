#!/usr/bin/python3
""" UTF Validation """


def validUTF8(data):
    """ validate UTF 8 """
    for number in data:
        if (number < 128):
            continue
        if number >> 6 & 0b11 == 0b10:
            continue
        if number >> 5 & 0b111 == 0b110:
            continue
        if number >> 4 & 0b1111 == 0b1110:
            continue
        if number >> 3 & 0b11111 == 0b11110:
            continue
        return False
    return True
