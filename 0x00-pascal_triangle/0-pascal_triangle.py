#!/usr/bin/python3
"""
pascal_triangle
"""
def pascal_triangle(n):  
    if n <= 0:  
        return []  
    
    triangle = []  
    
    for i in range(n):  
        row = [1] * (i + 1)  # Create a row with `i + 1` elements all set to 1  
        for j in range(1, i):  # Calculate values for positions that are not the edges  
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]  
        triangle.append(row)  
    
    return triangle
