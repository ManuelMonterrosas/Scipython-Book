"""
A molecule, A, reacts to form either B or C with first-order rate constants k1
and k2, respectively. That is,
        d[A]/dt = -(k1+k2)[A],
and so
        [A] = [A]_0 * e^-(k_1+k_2)*t,
where [A]_0 is the initial concentration of A. The product concentrations (starting
from 0) increase in the ratio [B]/[C] = k_1/k_2 and conservation of matter requires
[B] + [C] = [A]_0 - [A]. Therefore,
        [B] = k_1/(k_1+k_2) * [A]_0 * (1-e^-(k_1+k_2)*t)
        [C] = k_2/(k_1+k_2) * [A]_0 * (1-e^-(k_1+k_2)*t)
For a reaction with k_1 = 300 1/s and k_2 = 100 1/s, plot the concentrations of A, B 
and C against time given an initial concentration of reactant [A]_0 = 2.0 mol dm^(-3)
"""

import numpy as np
import matplotlib.pyplot as plt

k1 = 300  # 1/s
k2 = 100  # 1/s
init_a = 2.0  # mol dm^-3
time = np.linspace(0,0.02,1000)


conc_a = init_a*np.exp(-(k1+k2)*time)
conc_b = (k1/(k1+k2))*init_a*(1-np.exp(-(k1+k2)*time))
conc_c = (k2/(k1+k2))*init_a*(1-np.exp(-(k1+k2)*time))

plt.plot(1000*time, conc_a, label="[A]")
plt.plot(1000*time, conc_b, label="[B]")
plt.plot(1000*time, conc_c, label="[C]")
plt.xlabel("Time (ms)")
plt.legend()
plt.show()