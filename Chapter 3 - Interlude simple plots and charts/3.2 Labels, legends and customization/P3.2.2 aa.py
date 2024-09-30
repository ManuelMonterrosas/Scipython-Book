"""
A Gaussian integer is a complex number whose real and imaginary parts are
both integers. A Gaussian prime is a Gaussian integer x + iy such that either:
one of x and y is zero and the other is a prime number of the form 4n + 3 or
􀀀(4n + 3) for some integer n  0; or
 both x and y are nonzero and x2 + y2 is prime.
Consider the sequence of Gaussian integers traced out by an imaginary particle,
initially at c0, moving in the complex plane according to the following rule: it takes
integer steps in its current direction (1 in either the real or imaginary direction), but
turns left if it encounters a Gaussian prime. Its initial direction is in the positive real
direction (c = 1 + 0i ) x = 1; y = 0). The path traced out by the particle is called
a Gaussian prime spiral.
Write a program to plot the Gaussian prime spiral starting at c0 = 5 + 23i.
"""