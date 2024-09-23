"""
The value of pi may be approximated by Monte Carlo methods. Consider the
region of the xy-plane bounded by 0 <= x <= 1 and 0 <= y <= 1. By selecting a large
number of random points within this region and counting the proportion of them lying
beneath the function y = sqrt(1-x^2) describing a quarter-circle, one can estimate pi/4, this
being the area bounded by the axes and y(x). Write a program to estimate the value of pi
by this method.
Hint: use Python’s random module. The method random.random() generates a
(pseudo-)random number between 0. and 1. See Section 4.5.1 for more information.
"""

from random import random
from math import sqrt

n_max = 1000000  # number of points to simulate
count = 0
for i in range(n_max):
    x, y = random(), random()
    if y<sqrt(1-x**2):
        count += 1
pi_approx = 4*count/n_max
print(pi_approx)