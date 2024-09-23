"""
The table that follows gives the names, symbols, values, uncertainties and units
of some physical constants.
Use the string object’s format method to produce the following output:
"""

import math

kb = 1.380649e-23  # J/K
kb_units = 'J/K'
c = 2.99792458e8  # m/s
c_units = 'm/s'
h = 6.62607015e-34  # J*s
h_units = 'Js'
na = 6.02214076e23  # 1/mol
na_units = 'mol-1'
mue = -9.28476377e-24  # J/T
mue_unc = 2.3e-31  # uncertainty
mue_units = 'J/T'
g = 6.67430e-11  # N*m^2/kg^2
g_unc = 1.5e-15  # uncertainty
g_units = 'Nm^2/kg^2'

# a)
print('a)', '-'*40)
print(f'kB = {kb:.3e} {kb_units}')
# b)
print('b)', '-'*40)
print(f'G = {g:.16f} {g_units}')
# c)
print('c)', '-'*40)
format_c = '{:4s} = {: .4e} {:s}'
print(format_c.format('kB', kb, kb_units))
print(format_c.format('mu_e', mue, mue_units))
print(format_c.format('N_A', na, na_units))
print(format_c.format('c', c, c_units))
# d)
print('d)', '-'*40)
format_d = '=== {:4s} = {:+.2e} [{:>9s}] ==='
print(format_d.format('G', g, g_units))
print(format_d.format(u'\u03BC'+'e', mue, mue_units))
# e) got this one from the website
print('e)', '-'*40)
# e1) --------------------------------------------------------------
# The number of digits in the uncertainty to output
nsd_digits = 2
# Split the number in k * 10^e
exponent = int(math.floor(math.log10(abs(g))))
k = g / 10**exponent
# Calculate the uncertainty, relative to the same exponent
sd = g_unc / 10**exponent
# Calculate the number of decimal places to output in the constant, 
# such that the uncertainty has exactly nsd_digits digits
dp = int(-math.log(sd,10)) + nsd_digits
# Calculate the uncertainty digits as an integer
sd_digits = int(round(sd*10**dp))
print('G = {k:.{dp:d}f}({sd_digits:d})e{exponent:d} {units:s}'
            .format(k=k, dp=dp, sd_digits=sd_digits,
                    exponent=exponent, units=g_units))
# e2) --------------------------------------------------------------
# The number of digits in the uncertainty to output
nsd_digits = 2
exponent = int(math.floor(math.log10(abs(mue))))
k = mue / 10**exponent
sd = mue_unc / 10**exponent
dp = int(-math.log(sd,10)) + nsd_digits
sd_digits = int(round(sd*10**dp))
print('mu_e = {k:.{dp:d}f}({sd_digits:d})e{exponent:d} {units:s}'
            .format(k=k, dp=dp, sd_digits=sd_digits,
                    exponent=exponent, units=mue_units))
