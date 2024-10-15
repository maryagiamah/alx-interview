#!/usr/bin/python3
"""Write a method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """Write a method that determines if all the boxes can be opened."""
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key < len(boxes) and not unlocked[key]:
            unlocked[key] = True
            keys.update(boxes[key])
    return all(unlocked)
