"""
Heron’s method for calculating the square root of a number, S , is as follows:
starting with an initial guess, x_0, the sequence of numbers x_(n+1) = (1/2)*(x_n+S/x_n) are
successively better approximations to sqrt(S). Implement this algorithm to estimate the
square root of 2 117 519.73 to two decimal places and compare with the “exact” answer
provided by the math.sqrt method. For the purpose of this exercise, start with an initial
guess, x0 = 2000.
"""

import math

tol = 0.01  # tolerance
number = 2117519.73  # number for which I want to calculate the square root
a = 2000  # Initial guess
while True:
    b = 0.5*(a+number/a)
    if abs(a-b)<tol:
        break
    a = b

print('The number is {:.4f}'.format(number))
print('With Heron\'s formula I got: {:.4f}'.format(b))
print('With Python\'s sqrt I got: {:.4f}'.format(math.sqrt(number)))