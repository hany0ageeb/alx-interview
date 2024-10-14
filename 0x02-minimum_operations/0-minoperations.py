#!/usr/bin/python3
# 0-minoperations.py
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
    - Prototype: def minOperations(n)
    - Returns an integer
    - If n is impossible to achieve, return 0
"""


def minOperations(n: int) -> int:
    min_steps = float('inf')
    if n <= 1:
        return 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            steps = minOperations(i) + (n // i)
            if steps < min_steps:
                min_steps = steps
    return min_steps
