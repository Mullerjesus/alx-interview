#!/usr/bin/python3
"""
Solves the N Queens problem.
Usage: ./0-nqueens.py N
Where N is the size of the board and the number of queens to place.
"""

import sys


def print_solution(board):
    """
    Print the board configuration as a list of lists of coordinates.
    """
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


def is_safe(board, row, col):
    """
    Check if a queen can be placed at board[row][col].
    """
    # Check left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col):
    """
    Use backtracking to find all solutions for the N Queens problem.
    """
    if col >= len(board):
        print_solution(board)
        return True

    found_solution = False
    for row in range(len(board)):
        if is_safe(board, row, col):
            # Place the queen
            board[row][col] = 1
            # Recur to place the rest of the queens
            found_solution = solve_nqueens(board, col + 1) or found_solution
            # Backtrack
            board[row][col] = 0

    return found_solution


def nqueens(N):
    """
    Solve the N Queens problem for a given size N.
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0)


if __name__ == "__main__":
    # Check the number of arguments
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

    nqueens(N)
