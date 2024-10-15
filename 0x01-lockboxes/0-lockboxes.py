#!/usr/bin/python3
"""Write a method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """Write a method that determines if all the boxes can be opened."""
    flag = 1
    for i in range(1, len(boxes) - 1):
        flag = 1
        j = i
        while j > 0:
            if i in boxes[j - 1]:
                flag = 0
            j -= 1
    if flag:
        return False
    return True
