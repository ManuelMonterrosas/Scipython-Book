"""
The Earth Similarity Index (ESI) attempts to quantify the physical similarity
between an astronomical body (usually a planet or moon) and Earth. It is defined by

            ESI_j = product_{i=1 to n} (1-abs((x_ij-x_iE)/(x_ij+x_iE)))^(w_i/n)

where the parameters x_ij are described, and their terrestrial values, x_iE and weights, w_i,
are given in Table 2.14. The radius, density and escape velocities are taken relative to
the terrestrial values. The ESI lies between 0 and 1, with the values closer to 1 indicating
closer similarity to Earth (which has an ESI of exactly 1: Earth is identical to itself!).
The file ex2-6-g-esi-data.txt available from https://scipython.com/ex/bbc contains
the earlier mentioned parameters for a range of astronomical bodies. Use these
data to calculate the ESI for each of the bodies. Which has properties “closest” to those
of the Earth?
"""

def skip_lines(n, file):  # skips n lines in file f
    for i in range(n):
        file.readline()
    return

fname = r'C:\Users\manym\Documents\Coding\Scipython-book\Chapter 2 - The core python language I\2.6 File Input, Output\ex2-6-g-esi-data.txt'
f = open(fname, 'r')
skip_lines(4, f)
max_ESI = 0
earth_params = [1, 1, 1, 288]  # radius, density, escape_v, surface_t
weights = [0.57, 1.07, 0.7, 5.58]
n = len(earth_params)
for line in f.readlines():
    name = line[:15].strip()
    fields = line[15:].split()
    #radius, density, escape_v, surface_t = fields[1], fields[2], fields[4], fields[6]
    params = [float(fields[1]), float(fields[2]), float(fields[4]), float(fields[6])]
    # calculate ESI
    ESI_value = 1
    for i in range(n):
        ESI_value *= (1-abs((params[i]-earth_params[i])/(params[i]+earth_params[i])))**(weights[i]/n)
    if ESI_value > max_ESI:
        max_ESI = ESI_value
        max_name = name
f.close()
print("{object_name} is the object that is most similar to Earth. Its ESI is {object_ESI:.4f}".format(object_name=max_name, object_ESI=max_ESI))