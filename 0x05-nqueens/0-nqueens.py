#!/usr/bin/python3
import sys

def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)

def print_error_and_exit(message):
    print(message)
    sys.exit(1)

if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        print_usage_and_exit()

    # Validate the argument is an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print_error_and_exit("N must be a number")

    # Validate N is at least 4
    if N < 4:
        print_error_and_exit("N must be at least 4")

    # (Placeholder for your N-Queens solution implementation)
    print("N Queens Problem Solver")
