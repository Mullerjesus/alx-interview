#!/usr/bin/python3
"""
N-Queens Problem Solver
"""
import sys


class Position():
    """Represents a position on the chessboard"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_on_same_diagonal(self, other_pos):
        """Checks if two positions are on the same diagonal"""
        return abs(self.x - other_pos.x) == abs(self.y - other_pos.y)

    def is_on_same_line(self, other_pos):
        """Checks if two positions are on the same row or column"""
        return self.x == other_pos.x or self.y == other_pos.y

    def __str__(self):
        """String representation of the position"""
        return f"[{self.x}, {self.y}]"

    def toList(self):
        """Convert Position to list"""
        return [self.x, self.y]


def nqueens(size=""):
    """Solve the N-Queens problem"""
    if not size.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(size)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve and count solutions
    solutions = get_possible_solutions(n)
    for solution in solutions:
        print([pos.toList() for pos in solution])

    # Print total count of solutions
    print("OK")
    print(len(solutions))


def get_possible_solutions(n):
    """Return all valid N-Queens solutions"""
    return solve(n, [])


def solve(n, current_solution):
    """Recursive function to solve N-Queens"""
    row = len(current_solution)
    if row == n:
        # Return a complete solution
        return [current_solution]

    solutions = []
    for col in range(n):
        pos = Position(row, col)

        # Check if the position is safe
        if all(is_safe(pos, existing) for existing in current_solution):
            solutions.extend(solve(n, current_solution + [pos]))

    return solutions


def is_safe(new_pos, existing_pos):
    """Check if the new position does not conflict with the existing ones"""
    return not (new_pos.is_on_same_line(existing_pos) or new_pos.is_on_same_diagonal(existing_pos))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
