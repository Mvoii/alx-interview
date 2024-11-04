#!/usr/bin/python3
"""
    Main for test
"""

minOperations = __import__("0-minoperations").minOperations

n = 4
print("Min # of ops to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of ops to reach {} char: {}".format(n, minOperations(n)))
