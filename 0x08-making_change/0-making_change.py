#!/usr/bin/python3
"""change comes from within"""


def makeChange(coins, total):
    """Given a pile of coins of different values
    determine teh fewest number of coins needed
    to meet a given amount of total
    """
    if total < 1:
        return 0
    coins.sort()
    coins.reverse()
    fewest = 0
    for coin in coins:
        if total <= 0:
            break
        buff = total // coin
        fewest += buff
        total -= (buff * coin)
    if total != 0:
        return -1
    return fewest
