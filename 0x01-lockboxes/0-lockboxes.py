#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
     a method that determines if all the boxes can be opened.
     Args:
        boxes is a list of lists
    Return:
        True if all boxes can be opened, else return False
    """
    def visit(box):
        for key in box:
            if (key not in visited):
                visited.add(key)
                visit(boxes[key])
    visited = set([0])
    visit(boxes[0])
    return visited == set(range(0, len(boxes)))
