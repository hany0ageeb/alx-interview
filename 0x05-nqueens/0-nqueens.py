#!/usr/bin/python3
# 0-nqueens.py
"""
The N queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard.
Write a program that solves the N queens problem.
 - Usage: nqueens N
    - If the user called the program with the wrong number of arguments,
    print Usage: nqueens N, followed by a new line, and exit with the status 1
- where N must be an integer greater or equal to 4
    - If N is not an integer,
    print N must be a number,
    followed by a new line, and exit with the status 1
    - If N is smaller than 4,
    print N must be at least 4,
    followed by a new line, and exit with the status 1
- The program should print every possible solution to the problem
    - One solution per line
    - Format: see example
    - You don’t have to print the solutions in a specific order
- You are only allowed to import the sys module
"""
import sys


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at position (row, col)."""
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(N, row, board, solutions):
    """Try to solve the N-Queens problem using backtracking."""
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)
            board[row] = -1  # Backtrack


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize board (use a list where the index is the row and value is the column of the queen)
    board = [-1] * N  # Board of size N, all positions unfilled (-1)
    solutions = []
    solve_nqueens(N, 0, board, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
