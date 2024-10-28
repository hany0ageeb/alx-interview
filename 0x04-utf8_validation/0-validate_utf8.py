#!/usr/bin/python3
"""
Write a method that determines if a given data set
represents a valid UTF-8 encoding.
    - Prototype: def validUTF8(data)
    - Return: True if data is a valid UTF-8 encoding, else return False
    - A character in UTF-8 can be 1 to 4 bytes long
    - The data set can contain multiple characters
    - The data will be represented by a list of integers
    - Each integer represents 1 byte of data,
    therefore you only need to handle the 8 least significant
    bits of each integer
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    determines if a given data set represents a valid UTF-8 encoding.
    Args:
        data(list[int]):
    Return
        boolean: True data is a valid UTF-8 encoding
        otherwse return False
    """
    num_bytes = 0
    for byte in data:
        # Extract the last 8 bits of the integer
        byte &= 0b11111111
        if num_bytes == 0:
            # 0xxxxxxxx
            if (byte >> 7) == 0b0:
                num_bytes = 0  # 1 byte
            # 110xxxxxxxx
            elif (byte >> 5) == 0b110:
                num_bytes = 1  # 2 bytes
            elif (byte >> 4) == 0b1110:
                num_bytes = 2  # 3 bytes
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= -1
    return num_bytes == 0
