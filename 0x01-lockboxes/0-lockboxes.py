#!/usr/bin/python3
"""Write a method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """Write a method that determines if all the boxes can be opened."""
    for i in range(1, len(boxes)):
        j = i - 1
        flag = 1
        while j >= 0:
            if i in boxes[j]:
                flag = 0
            j -= 1
    if flag:
        return False
    return True
