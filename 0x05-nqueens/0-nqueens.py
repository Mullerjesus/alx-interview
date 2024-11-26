#!/usr/bin/python3
"""
N Queens Problem Solver
"""

import sys


def print_usage_and_exit():
    """Print usage and exit with status 1"""
    print("Usage: nqueens N")
    sys.exit(1)


def print_number_error_and_exit():
    """Print number error and exit with status 1"""
    print("N must be a number")
    sys.exit(1)


def print_minimum_error_and_exit():
    """Print minimum error and exit with status 1"""
    print("N must be at least 4")
    sys.exit(1)


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check this column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    """
    Solve the N Queens problem and return all solutions
    """
    def backtrack(row):
        """Recursive backtracking"""
        if row == n:
            solutions.append([[i, board[i]] for i in range(n)])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    board = [-1] * n  # Initialize board with -1
    solutions = []
    backtrack(0)
    return solutions


def main():
    """
    Main function to parse input and print solutions
    """
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print_number_error_and_exit()

    if n < 4:
        print_minimum_error_and_exit()

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
