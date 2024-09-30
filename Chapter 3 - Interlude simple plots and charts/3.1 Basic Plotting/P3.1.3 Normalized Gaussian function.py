"""
The normalized Gaussian function centered at x = 0 is
        g(x) = (1/(sigma*sqrt(2*pi)))*exp(-x**2/(2*sigma**2))
Plot and compare the shapes of these functions for standard deviations sigma = 1, 1.5 and 2.
"""

import numpy as np
import matplotlib.pyplot as plt

def norm_Gauss(x, sigma):
    """ Returns the normalized Gaussian function centered at x=0 when given x and sigma
    """
    return (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-x**2/(2*sigma**2))

x_range = np.linspace(-10, 10, 1000)
sigmas = np.array([1, 1.5, 2])

for dev in sigmas:
    plt.plot(x_range, norm_Gauss(x_range, dev), label=f"$\sigma$ = {dev:.1f}")
plt.legend()
plt.show()