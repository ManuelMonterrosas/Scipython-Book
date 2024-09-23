"""
Given the elements of a 3 x 3 matrix as the nine variables a11, a12, . . . , a33,
produce a string representation of the matrix using formatting methods, (a) assuming
the matrix elements are (possibly negative) real numbers to be given to one decimal
place; (b) assuming the matrix is a permutation matrix with integer entries taking the
values 0 or 1 only. For example,
"""

import random

# First I will create the matrices s_a and s_b with random numbers according to the instructions
s_a = []  # this 3x3 matrix will have float numbers between -1 and 1.
s_b = []  # this 3x3 matrix will have integers 0 or 1

for i in range(3):
    aux1 = []
    aux2 = []
    for j in range(3):
        aux1.append(random.random()*2-1)
        aux2.append(random.randint(0, 1))
    s_a.append(aux1)
    s_b.append(aux2)

print(s_a)
format_a = '[ {:4.1f} {:4.1f} {:4.1f} ]'
print(format_a.format(s_a[0][0], s_a[0][1], s_a[0][2]), 
      format_a.format(s_a[1][0], s_a[1][1], s_a[1][2]), 
      format_a.format(s_a[2][0], s_a[2][1], s_a[2][2]), 
      sep='\n')

print(s_b)
format_b = '[ {} {} {}]'
print(format_b.format(s_b[0][0], s_b[0][1], s_b[0][2]), 
      format_b.format(s_b[1][0], s_b[1][1], s_b[1][2]), 
      format_b.format(s_b[2][0], s_b[2][1], s_b[2][2]), 
      sep='\n')