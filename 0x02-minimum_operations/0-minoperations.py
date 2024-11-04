#!/usr/bin/python3
"""Module for 0-minops"""


def minOperations(n):
    """
    minOps
    Gets least num of ops needed to result in exactly n H characters
    """
    if n < 2:
        return 0
    ops, root = 0, 2
    while root <= n:
        if n % root == 0:
            ops += root
            n = n / root
            root -= 1
        root += 1
    return ops
