""" The seedhead of a sunflower may be modeled as follows. Number the n seeds
s = 1, 2, ..., n and place each seed a distance r = sqrt(s) from the origin, rotated
theta = 2*pi*s/phi from the x axis, where phi is some constant. The choice nature 
makes for phi is the golden ratio, phi = (1+sqrt(5)/2, which maximizes the packing 
efficiency of the seeds as the seedhead grows.
Write a Python program to plot a model sunflower seedhead. (Hint: use polar coordinates.)
"""

import numpy as np
import matplotlib.pyplot as plt

n = 200  # number of seeds to plot
phi = (1+np.sqrt(5))/2 # packing constant, in this case golden ratio
r = []
theta = []
# Calculate r and theta for every seed
for i in range(n):
    r = np.append(r, np.sqrt(i+1))
    theta = np.append(theta, 2*np.pi*(i+1)/phi)

# Alternatively, without for loop
# s = np.linspace(0, n-1, n)
# r = np.sqrt(s)
# theta = 2 * np.pi * s / phi

# plt.polar(theta, r, marker='o', linestyle='', markersize=12, color='r')
plt.polar(theta, r, marker='o', markersize=12, color='r')  # looks cooler
plt.show()