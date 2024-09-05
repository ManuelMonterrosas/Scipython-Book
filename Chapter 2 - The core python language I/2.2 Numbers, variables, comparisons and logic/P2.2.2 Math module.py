"""
Some fun with the math module:
(a) What is special about the numbers sin(2017*2^(1/5)) and (pi+20)^i
(b) What happens if you try to evaluate an expression, such as e^1000, which generates a number larger than the largest
floating-point number that can be represented in the default double precision? What if you restrict your calculation to
integer arithmetic (e.g. by evaluating 1000!)?
(c) What happens if you try to perform an undefined mathematical operation such as division by zero?
(d) The maximum representable floating-point number in IEEE-754 double precision is about 1.8x10^308. Calculate the
length of the hypotenuse of a right-angled triangle with opposite and adjacent sides 1.5x10^200 and 3.5x10^201
    (i) using the math.hypot() function directly and
    (ii) without using this function.
"""

import math

# a) they are both roughly -1
print(math.sin(2017*2**(1/5)))
print((math.pi+20)**1j)

# b) for the float we get "error, number too large", but the integer seems to have no problem even up to 100,000!
# print(math.e**1000) # this gives error
print(math.factorial(1000))

# c) you get the error "division by zero"
# print(10/0) # this gives error

# d) the built-in function can calculate the result whereas the normal definition fails!
# This must be because a^2 and b^2 are larger than the maximum float number allowed
# The function hypot must use an approximation where it does not need to calculate a^2 and b^2
a = 1.5*10**200
b = 3.5*10**201
print(math.hypot(a, b))
print(math.sqrt(a**2 + b**2))  # this gives error
