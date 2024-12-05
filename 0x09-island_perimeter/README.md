Island Perimeter Project
This project focuses on solving the "Island Perimeter" problem by calculating the perimeter of an island represented in a grid format. The grid is a 2D list where 1 represents land and 0 represents water. The goal is to write a Python function to compute the perimeter of the land, taking into account the grid's structure and neighboring cells.

Project Requirements
Implement a function island_perimeter(grid) that returns the perimeter of the island defined in the grid.
The grid is a list of lists of integers:
0 represents water
1 represents land
Each cell in the grid is a square with a side length of 1.
Cells are connected either horizontally or vertically, but not diagonally.
The grid dimensions do not exceed 100 in width and height.
The grid is entirely surrounded by water.
There is only one island, and it does not contain any lakes (i.e., water inside the island that is not surrounded by land).

Function Signature
def island_perimeter(grid):
Parameters:
grid: A list of lists of integers representing the grid layout.
Returns:
An integer representing the perimeter of the island.
Example Usage
The following is an example of how to use the function:

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12

Contribution
This Project is Worked by Muluken Eshetu, Student of ALX-SE Cohort 22
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
This project is part of the ALX Specialization curriculum. Special thanks to the ALX team for providing the resources and guidance throughout this project.
