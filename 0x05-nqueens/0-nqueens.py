#!/usr/bin/python3
"""
    Nqueens
"""
import sys


solutions = []
"""
    the list of possile solutions to teh problem
"""
n = 0
"""
    The size of the board
"""
pos = None
"""
    list of posible positions on teh board
"""


def get_input():
    """
    retrieves and validates the args

    Returns:
        int: the size of the chessboard
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must  be atleast 4")
        sys.exit(1)
    return n


def is_attacking(pos0, pos1):
    """
    checks if the positions of the two queens are in attacking mode

    Args:
        pos0 (list or tuple):The first queen's position
        pos1 (list or tuple): The position of teh second queen

    Returns:
        bool: True if attacking, else False
    """
    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def group_exists(group):
    """
    checks if a group exists in the list of solutions

    Args:
        groups (list of ints): A group of possible positions

    Returns:
        bool: true if it exists, else false
    """
    global solutions
    for stn in solutions:
        i = 0
        for stn_pos in stn:
            for grp_pos in group:
                if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
                    i += 1
        if i == n:
            return True
    return False


def build_solution(row, group):
    """
    Builds a solution for the n queens problem

    Args:
        row (int): The current row in the chessboard
        group (list of lists of ints): The group of valid positions
    """
    global solutions
    global n
    if row == n:
        tmp0 = group.copy()
        if not group_exists(tmp0):
            solutions.append(tmp0)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip(list([pos[a]]) * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(pos[a].copy())
            if not any(used_positions):
                build_solution(row + 1, group)
            group.pop(len(group) - 1)


def get_solutions():
    """
    Gets the solutions for the given chessboard size
    """
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n**2)))
    a = 0
    group = []
    build_solution(a, group)
    print("getting soln")


n = get_input()
get_solutions()
for solution in solutions:
    print(solution)
