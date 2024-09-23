"""
The iterative weak acid approximation determines the hydrogen ion concentration,
[H+], of an acid solution from the acid dissociation constant, K_a, and the acid
concentration, c, by successive application of the formula
                [H+]_(n+1) = sqrt(K_a*(c-[H+]_n))
starting with [H+]_0 = 0. The iterations are continued until [H+] changes by less than
some predetermined, small tolerance value.
Use this method to determine the hydrogen ion concentration, and hence the pH (=
- log10[H+]) of a c = 0.01 M solution of acetic acid (Ka = 1.78 x 10^-5). Use the
tolerance TOL = 1.e-10.
"""
import math

def Hplus(K, C, H):
    return math.sqrt(K*(C-H))

c, ka = 0.01, 1.78E-5
tol = 1E-10
a = 0  # the current H+ value

while True:
    b = Hplus(ka, c, a)  # calculate next value using the previous one
    dif = abs(a-b)  # calculate the diference
    if dif<tol:
        break
    a = b

ph = -math.log10(b)
print("The pH is {:.2f}".format(ph))
