#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """rotate_2d_matrix
    """
    for deg in range(90):
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        while left < right and top < bottom:
            prev = matrix[top + 1][left]
            for i in range(left, right + 1):
                curr = matrix[top][i]
                matrix[top][i] = prev
                prev = curr
            top += 1
            for i in range(top, bottom + 1):
                curr = matrix[i][right]
                matrix[i][right] = prev
                prev = curr
            right -= 1
            for i in range(right, left-1, -1):
                curr = matrix[bottom][i]
                matrix[bottom][i] = prev
                prev = curr
            bottom -= 1
            for i in range(bottom, top-1, -1):
                curr = matrix[i][left]
                matrix[i][left] = prev
                prev = curr
            left += 1
