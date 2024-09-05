"""
Some languages provide a sign(a) function which returns -1 if its argument,
a, is negative and 1 otherwise. Python does not provide such a function, but the math
module does include a function math.copysign(x, y), which returns the absolute value
of x with the sign of y. How would you use this function in the same way as the missing
sign(a) function?
"""
from math import copysign


# This function should return -1 or 1, depending on the sign of a
def sign(a):
    return copysign(1, a)


print(sign(10))
print(sign(-10))
