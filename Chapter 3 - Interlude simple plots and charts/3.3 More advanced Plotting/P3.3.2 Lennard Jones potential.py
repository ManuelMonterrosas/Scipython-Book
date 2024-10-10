""" A simple model for the interaction potential between two atoms as a function
of their distance, r, is that of Lennard-Jones:
                U(r) = B/r^12 - A/r^6 
where A and B are positive constants.
For Argon atoms, these constants may be taken to be A = 1.024*10^23 J*nm^6 and
B = 1.582*10^26 J*nm^12.

(a) Plot U(r). On a second y-axis on the same figure, plot the interatomic force
                F(r) = -dU/dr = 12B/r^13 - 6A/r^7
Your plot should show the “interesting” part of these curves, which tend rapidly
to very large values at small r.
Hint: life is easier if you divide A and B by Boltzmann's constant, 1.381*10^-23 JK^-1
so as to measure U(r) in units of K. What is the depth, epsilon, and location,
r0, of the potential minimum for this system?

(b) For small displacements from the equilibrium interatomic separation (where F =
0), the potential may be approximated to the harmonic oscillator function,
                V(r) = (1/2)*k(r-r0)^2 + epsilon
where
                k = |d^2U/dr^2|_r0 = 156B/r^14_0 - 42A/r^8_0
Plot U(r) and V(r) on the same diagram.
"""

import numpy as np
import matplotlib.pyplot as plt

case = 2
if case == 1:  # simple Lennard-Jones
    # Define constants
    KB = 1.381e-23  # in J*K^-1
    A = 1.024e-23/KB  # in K*nm^6
    B = 1.582e-26/KB  # in K*nm^12

    # Determine area of interest
    r_0 = (2*B/A)**(1/6)  # where U(r) is minimum and F=0, in nm. Value: 0.38 nm
    U_min = B/r_0**12 - A/r_0**6  # minimum potential U(r_0), in K. Value: -119.98 K
    print(f"The potential depth is {U_min:.2f} K, found at {r_0:.2f} nm")

    # Set variables according to area of interest
    r = np.linspace(0.3, 1, 1000)  # in nm
    U_pot = B/r**12 - A/r**6  # in K
    F_for = 12*B/r**13 - 6*A/r**7  # in K/nm

    
    line1 = plt.plot(r, U_pot, 'b', label='Potential')
    plt.ylabel('Potential [K]')
    plt.xlim(0.3, 0.8)
    plt.ylim(-150, 100)

    plt.twinx()
    line2 = plt.plot(r, F_for, '--r', label='Force')
    plt.ylabel('Force [K/nm]')
    plt.xlim(0.3, 0.8)
    plt.ylim(-1000, 1000)

    # To get labels in the same legend
    lines = line1 + line2
    labels = []
    for line in lines:
        labels.append(line.get_label())
    plt.legend(lines, labels)
    plt.tight_layout()
    plt.show()

if case == 2:  # small displacement case
    # For small displacements, we need to approximate the potental as a harmonic oscillator
    # Define constants
    KB = 1.381e-23  # in J*K^-1
    A = 1.024e-23/KB  # in K*nm^6
    B = 1.582e-26/KB  # in K*nm^12
    r_0 = (2*B/A)**(1/6)  # where U(r) is minimum and F=0, in nm
    U_min = B/r_0**12 - A/r_0**6  # minimum potential U(r_0), in K. Value: -119.98 K
    k = 156*B/r_0**14 -42*A/r_0**8  # d^2U/dr^2 at r=r_0, in K/r^2

    # Set variables according to area of interest
    r = np.linspace(r_0*0.8, r_0*1.2, 1000)  # small displacement around r_0 in nm
    U_pot = B/r**12 - A/r**6  # in K
    V_pot = 0.5*k*(r-r_0)**2 + U_min  # in K

    # Plot both U(r) and V(r) for small displacement around r_0
    plt.plot(r-r_0, U_pot, 'b-', label="U(r)")
    plt.plot(r-r_0, V_pot, 'r--', label="V(r)")
    plt.ylim(-120, 0)
    plt.legend()
    plt.xlabel(r"$\Delta$r [nm]")
    plt.ylabel("Potential/$k_B$ [K]")
    plt.show()