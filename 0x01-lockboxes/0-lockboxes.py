#!/usr/bin/python3
"""L0ckb0x3s"""


def canUnlockAll(boxes):
    """
    a method that determines if all boxes can be opened

    :param boxes:
    :return: True or false
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)

    if len(unlocked) == len(boxes):
        return True
    return False
