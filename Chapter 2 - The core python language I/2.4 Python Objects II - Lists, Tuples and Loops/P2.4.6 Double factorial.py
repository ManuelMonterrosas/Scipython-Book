"""
The factorial function, n! = 1 x 2 x 3 x ... x (n - 1) x n is the product of the first n
positive integers and is provided by the math module’s factorial method. The double
factorial function, n!!, is the product of the positive odd integers up to and including n
(which must itself be odd).
Write a routine to calculate n!! in Python.
As a bonus exercise, extend the formula to allow for even n as a product of only even numbers
"""

def single_factorial(n):  # not required, but I like the recursive solution and wanted to have it written down
    if n>1:
        return n*single_factorial(n-1)
    else:
        return 1

def double_factorial(n):  # for odd, only get odd product. For even, only get even
    if n>2:
        return n*double_factorial(n-2)
    elif n==2:
        return 2
    elif n==1:
        return 1

print(single_factorial(6))
print(double_factorial(5))
print(double_factorial(6))