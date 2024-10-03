#!/usr/bin/python3
"""
pascal_triangle
"""
def pascal_triangle(n):  
    if n <= 0:  
        return []  
    
    triangle = [[1]]  # Start with the first row  

    for i in range(1, n):  # Loop to create each subsequent row  
        row = [1]  # First element is always 1  
        last_row = triangle[i - 1]  # Get the last row already created  

        # Calculate the inner elements of the triangle row  
        for j in range(1, i):  
            row.append(last_row[j - 1] + last_row[j])  
        
        row.append(1)  # Last element is always 1  
        triangle.append(row)  # Add the new row to the triangle  
    
    return triangle
