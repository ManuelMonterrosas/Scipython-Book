"""
The annual risk of death (given as “1 in N”) for men and women in the UK in
2005 for different age ranges is given in the table below. Use pyplot to plot these data
on a single chart.
"""

import numpy as np
import matplotlib.pyplot as plt

age_ranges = np.array(["<1", "1-4", "5-14", "15-24", "25-34", "35-44", "45-54", "55-64", "65-74", "75-84", ">84"])
risk_female = np.array([227, 5376, 10417, 4132, 2488, 1106, 421, 178, 65, 21, 7])
risk_male = np.array([177, 4386, 8333, 1908, 1215, 663, 279, 112, 42, 15, 6])

plt.plot(age_ranges, risk_female, label="Female")
plt.plot(age_ranges, risk_male, label="Male")
plt.title("Risk of death in the UK for 2005, given in 1/N")
plt.legend()
plt.show()