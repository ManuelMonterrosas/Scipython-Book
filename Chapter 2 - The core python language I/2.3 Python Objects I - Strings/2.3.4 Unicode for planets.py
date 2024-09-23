"""
Find the Unicode code points for the planet symbols listed on the NASA website
(https://solarsystem.nasa.gov/resources/680/solar-system-symbols/) which mostly
fall within the hex range 2600–26FF: Miscellaneous Symbols (https://www.unicode.
org/charts/PDF/U2600.pdf) and output a list of planet names and symbols.
"""

list_names = ['Sun', 'Mercury', 'Venus', 'Earth', 'Moon', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
list_symbols = ['\u2609', '\u263F', '\u2640', '\u2295', '\u263E', '\u2642', '\u2643', '\u2644', '\u26E2', '\u2646', '\u2647']

for i in range(len(list_names)): # we haven't seen loops, but it is here for simplicity
    print('{:>10s}: {}'.format(list_names[i], list_symbols[i]))