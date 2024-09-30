"""
Write a function, sinm_cosn, which returns the value of the following definite 
integral for integers m,n>1
        *Complicated integral, see book*
"""

import math

def sinm_cosn(m:int, n:int):
    """ Returns the value of a definite integral for integers m,n>1
    """
    if m%2==0 and n%2==0:
        result = (math.pi/2)*double_factorial(m-1)*double_factorial(n-1)/double_factorial(m+n)
    else:
        result = double_factorial(m-1)*double_factorial(n-1)/double_factorial(m+n)
    return result

def double_factorial(n):  # for odd, only get odd product. For even, only get even product
    """ Returns the value n*(n-2)*(n-4)*...*3*1 or n*(n-2)*(n-4)*...*4*2 for an integer n
    """
    if n>2:
        return n*double_factorial(n-2)
    elif n==2:
        return 2
    elif n==1:
        return 1
    
print(sinm_cosn(5,7))
print(sinm_cosn(5,7))