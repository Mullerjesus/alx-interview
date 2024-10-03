#!/usr/bin/python3
'''pascal triangle'''


def pascal_triangle(n):
    '''
    returns an integers representing the Pascal’s triangle
    arguments
             n: number of pascal triangle a user wants
    '''
    triangle = []
    if n == 0:
        return lists
    for i in range(n):
        triangle.append([])
        triangle[i].append(1)
        if (i > 0):
            for j in range(1, i):
        triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            triangle[i].append(1)
    return triangle
