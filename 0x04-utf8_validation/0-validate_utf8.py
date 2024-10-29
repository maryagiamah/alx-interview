#!/usr/bin/python3
"""Write a method that determines
if a given data set represents a UTF-8 encoding
"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    ascii_bit = 1 << 7
    cont_bit = 0
    for val in data:
        if cont_bit == 0:
            while val & ascii_bit:
                ascii_bit = ascii_bit >> 1
                cont_bit += 1
            if not cont_bit:
                continue
            if cont_bit > 4 or cont_bit == 1:
                return False
        else:
            if not (val & (1 << 7)):
                return False
        cont_bit -= 1
    if cont_bit == 0:
        return True
    return False
