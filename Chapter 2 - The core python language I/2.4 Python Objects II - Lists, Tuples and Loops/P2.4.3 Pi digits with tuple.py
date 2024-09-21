"""
Using a tuple of strings naming the digits 0–9, create a Python program which
outputs the representation of Pi as read aloud to eight decimal places:
three point one four one five nine two six five (3.14159265)
"""

from math import pi

digits = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
pi_string = '{:.8f}'.format(pi)
pi_decimal = pi_string[2:]
to_show = ['three', 'point']

for i in range(len(pi_decimal)):
    to_show.append(digits[int(pi_decimal[i])])

# print(to_show)
print(*to_show, sep=' ') # to print nicely with space
