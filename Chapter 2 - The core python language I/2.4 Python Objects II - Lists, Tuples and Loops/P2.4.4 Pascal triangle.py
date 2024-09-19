"""
Write a program to output a nicely formatted depiction of the first eight rows
of Pascal’s triangle.
"""

def pascal_row(n): # n represents row number to calculate
    if n > 1:
        aux_row = pascal_row(n-1)
        aux_row.insert(0, 0)  # add a 0 in the beginning
        aux_row.append(0)  # and a 0 in the end
        actual_row = []
        for i in range(n):
            actual_row.append(aux_row[i] + aux_row[i+1])
        return actual_row
    else:
        return [1]

def pascal_triangle(n):  # calculates all the pascal rows up to n, then prints nicely
    aux_matrix = []
    count = 1
    # calculates
    for i in range(n):
        aux_matrix.append(pascal_row(count))
        count += 1
    # then prints
    for i in range(len(aux_matrix)):
        print(int((3*n-3*(i+1))/2)*' ', end='') # this is just to set the padding space before each row
        for j in range(len(aux_matrix[i])):
            print('{:2d}'.format(aux_matrix[i][j]), end=' ')
        print('')
    return

#print(pascal_row(5))
pascal_triangle(8)