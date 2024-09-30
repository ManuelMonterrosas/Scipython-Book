"""
Tetration may be thought of as the next operator after exponentiation. Thus,
where X x N can be written as the sum X + X + X + ... + X with N terms, and X^N is the
multiplication of N factors X, the expression written ^N X is equal to the repeated
exponentiation involving N occurrences of X:
^N X = X^X^X...^X
For example, ^4 2 = 2^2^2^2 = 2^2^4 = 2^16 = 65536. Note that the exponential “tower” is
evaluated from top to bottom.
Write a recursive function to calculate ^N X and test it (for small, positive real values of
X and non-negative integers N: tetration generates very large numbers)!
How many digits are there in ^3 5? In ^5 2?
"""

import math

def tetration(N: int, X:float):
    """ Returns the tetration ^N X = X^X^X...^X
    """
    if N == 1:
        return X
    return X**tetration(N-1, X)

print(tetration(4,2))
print(len(str(tetration(3,5))))
print(len(str(tetration(5,2))))