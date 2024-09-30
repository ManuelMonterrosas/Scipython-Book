"""
Plot the functions
    f1(x) = ln(1/cos^2(x))
and 
    f2(x) = ln(1/sin^2(x))
on 1000 points across the range -20 <= x <= 20. What happens to these functions at
x = n*Pi/2 (n = 0, +-1, +-2, ...)? What happens in your plot of them?
"""

import matplotlib.pyplot as plt
import numpy as np

x_range = np.linspace(-20, 20, 1000)
y1_range = np.log(1/(np.cos(x_range))**2)
y2_range = np.log(1/(np.sin(x_range))**2)

plt.plot(x_range, y1_range)
plt.plot(x_range, y2_range)
plt.show()

# the functions are not defined at x=n*pi/2, but the plot seems continuous (peak formation)
