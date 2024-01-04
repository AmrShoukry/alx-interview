#!/usr/bin/python3
""" UTF 8 validation """


def validUTF8(data):
    """ valid utf 8 function """
    for number in data:
        if (number >= 256 and number < 384):
            return False
    return True
