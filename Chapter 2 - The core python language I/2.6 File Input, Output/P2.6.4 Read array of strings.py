"""
Write a program to read in a two-dimensional array of strings into a list of
lists from a file in which the string elements are separated by one or more spaces. The
number of rows, m, and columns, n, may not be known in advance of opening the file.
For example, the text file
A B C D
E F G H
I J K L
should create an object, grid, as
[['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K', 'L']]
Read like this, grid contains a list of the array’s rows. Once the array has been read in,
write loops to output the columns of the array:
[['A', 'E', 'I'], ['B', 'F', 'J'], ['C', 'G', 'K'], ['D', 'H', 'L']]
Harder: also output all its diagonals read in one direction:
[['A'], ['B', 'E'], ['C', 'F', 'I'], ['D', 'G', 'J'], ['H', 'K'], ['L']]
and the other direction:
[['D'], ['C', 'H'], ['B', 'G', 'L'], ['A', 'F', 'K'], ['E', 'J'], ['I']]
"""

import os

cwd = os.getcwd()
fname = cwd + r'\Chapter 2 - The core python language I\2.6 File Input, Output\array.txt'
f = open(fname, 'r')
grid = []
for line in f.readlines():
    grid.append(line.split())
f.close()
# Output the columns of the array
print([[row[column] for row in grid] for column in range(len(grid[0]))])
# Output diagonals in one direction. Start from the upper-left corner, inverse diagonals.
# Here i,j sum is constant per diagonal
diag_backwards = []
for sum in range(len(grid)+len(grid[0])-1):
    diag_aux = []
    for row_ind in range(len(grid)):
        column_ind = sum - row_ind
        if column_ind >= 0  and column_ind <= len(grid[0])-1:
            diag_aux.append(grid[row_ind][column_ind])
    diag_backwards.append([diag_aux])
print(diag_backwards)
# And the other direction. Start from the upper-right corner, forward diagonals. 
# Here i,j difference is constant per diagonal
diag_forwards = []
for diff in range(-len(grid[0])+1, len(grid)):  # I am doing m-n (row-column)
    diag_aux = []
    for row_ind in range(len(grid)):
        column_ind = row_ind - diff
        if column_ind >= 0  and column_ind <= len(grid[0])-1:
            diag_aux.append(grid[row_ind][column_ind])
    diag_forwards.append([diag_aux])
print(diag_forwards)