#!/usr/bin/python3
"""Write a method that determines
if a given data set represents a UTF-8 encoding
"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    ascii_bit = 1 << 7
    cont_bit = 0
    for val in data:
        ascii_bit = 1 << 7
        if cont_bit == 0:
            while val & ascii_bit:
                ascii_bit >>= 1
                cont_bit += 1
            if cont_bit == 0:
                continue
            if cont_bit > 4 or cont_bit == 1:
                return False
        else:
            if not ((val & (1 << 7)) and not(val & (1 << 6))):
                return False
        cont_bit -= 1
    return cont_bit == 0
