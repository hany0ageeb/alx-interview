#!/usr/bin/python3
"""
module documentation
"""


def pascal_triangle(n):
    """
    function to return pascal's triangle
    """
    if (n <= 0):
        return []
    elif (n == 1):
        return [[1]]
    elif (n == 2):
        return [[1], [1, 1]]
    else:
        result = [[1], [1, 1]]
        for row in range(2, n):
            rw = []
            for col in range(0, row + 1):
                if (col == 0 or col == row):
                    rw.append(1)
                else:
                    rw.append(result[row - 1][col - 1] + result[row - 1][col])
            result.append(rw)
        return result