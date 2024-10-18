#!/usr/bin/python3
"""minOperations"""


def minOperations(n):
    """minOperations"""

    if n <= 1:
        return 0

    no_op = 0
    div_sor = 2

    while n > 1:
        while n % div_sor == 0:
            no_op += div_sor
            n = n // div_sor
        div_sor += 1

    return no_op
