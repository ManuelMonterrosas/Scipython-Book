""" A spiral may be considered to be the figure described by the motion of a point
on an imaginary line as that line pivots around an origin at constant angular velocity. If
the point is fixed on the line, then the figure described is a circle.
(a) If the point on the rotating line moves from the origin with constant speed, its
position describes an Archimedean spiral. In polar coordinates, the equation of
this spiral is r = a + b*theta. Use pyplot to plot the spiral defined by a = 0; b = 2 for
0 <= theta <= 8*pi.
(b) If the point moves along the rotating line with a velocity that increases in proportion
to its distance from the origin, the result is a logarithmic spiral, which may be
written as r = a^theta. Plot the logarithmic spiral defined by a = 0.8 for 0 <= theta <= 8*pi.
The logarithmic spiral has the property of self-similarity: with each 2*pi whorl,
the spiral grows but maintains its shape. Logarithmic spirals occur frequently in
nature, from the arrangements of the chambers of nautilus shells to the shapes of
galaxies.
"""

import numpy as np
import matplotlib.pyplot as plt

case = 2

if case == 0:  # circle
    theta = np.linspace(0, 8*np.pi, 1000)
    r = 5 + 0*theta # radius
    plt.polar(theta, r)
    plt.show()
if case == 1:  # Archimedean spiral
    a = 0  # translation parameter
    b = 2  # growth parameter
    theta = np.linspace(0, 8*np.pi, 1000)
    r1 = a + b*theta
    # r2 = b*theta  # a=0 as reference
    r2 = a + 2*b*theta  # b=2b
    plt.polar(theta, r1)
    plt.polar(theta, r2)
    plt.show()
if case == 2:  # Logarithmic spiral
    a = 0.8  # growth parameter
    theta = np.linspace(0, 8*np.pi, 1000)
    r1 = a**theta
    r2 = (a*0.95)**theta
    plt.polar(theta, r1)
    plt.polar(theta, r2)
    plt.show()
