#!/usr/bin/python3
"""Write a method that determines
if a given data set represents a UTF-8 encoding
"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    try:
        byt_str = bytes(data)
        byt_str.decode("utf-8")
        return True
    except (ValueError, UnicodeDecodeError):
        return False
