"""
The table that follows gives the names, symbols, values, uncertainties and units
of some physical constants.
Use the string object’s format method to produce the following output:
"""

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
print(f'kB = {kb:.3e} {kb_units}')
# b)
print(f'G = {g:.16f} {g_units}')
# c)
print('{name:4s} = {value: .4e} {unit:s}'.format(name='kB', value=kb, unit=kb_units))
print('{name:4s} = {value: .4e} {unit:s}'.format(name='mu_e', value=mue, unit=mue_units))
print('{name:4s} = {value: .4e} {unit:s}'.format(name='N_A', value=na, unit=na_units))
print('{name:4s} = {value: .4e} {unit:s}'.format(name='c', value=c, unit=c_units))
# d)
# e)
