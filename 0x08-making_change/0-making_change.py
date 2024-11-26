#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total.
Prototype: def makeChange(coins, total)
Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
You can assume you have an infinite number of each denomination
of coin in the list
Your solution’s runtime will be evaluated in this task
"""


def minCoinsRecur(i, total, coins):
    """minCoinsRecur
    """
    if total == 0:
        return 0
    if total < 0 or i == len(coins):
        return float('inf')
    take = float('inf')
    if coins[i] > 0:
        take = minCoinsRecur(i, total - coins[i], coins)
        if take != float('inf'):
            take += 1
    noTake = minCoinsRecur(i + 1, total, coins)
    return min(take, noTake)


def makeChange(coins, total):
    """makeChange
    """
    if total <= 0:
        return 0
    ans = minCoinsRecur(0, total, coins)
    return ans if ans != float('inf') else -1
