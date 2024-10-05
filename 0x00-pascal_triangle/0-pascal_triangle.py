#!/usr/bin/python3

"""Pascal Triangle"""


def pascal_triangle(n):
    """ Returns list of list """
    if n <= 0:
        return [[]]

    pasc_arr = [[1]]
    for idx in range(1, n):
        pasc_arr.extend([[1]])
        for j in range(len(pasc_arr[idx - 1]) - 1):
            pasc_arr[idx].append(
                pasc_arr[idx - 1][j] + pasc_arr[idx - 1][j + 1])
        pasc_arr[idx].append(1)
    return pasc_arr
