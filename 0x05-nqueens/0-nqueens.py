#!/usr/bin/python3
""" nqueens implementation module"""
import sys


def nqueens(n):
    """returns the possible placements of the queens"""
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def solve(queens, difference, add):
        """applies the backtracking algorithm recursively and generates
            possible possitons
        """
        p = len(queens)
        if p == n:
            result.append(queens)
            return

        for q in range(n):
            if q not in queens and p-q not in difference and p+q not in add:
                solve(queens+[q], difference+[p-q], add+[p+q])

    result = []
    solve([], [], [])

    return result


if len(sys.argv) != 2:
    print("Usage:  nqueens N")
    sys.exit(1)
result = [solution for solution in nqueens(sys.argv[1])]
rs = []
for j in result:
    temp = []
    for i in range(len(j)):
        temp.append([i, j[i]])
    rs.append(temp)
for r in rs:
    print(r)
