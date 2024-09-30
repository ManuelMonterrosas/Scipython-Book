"""
A right regular pyramid with height h and a base consisting of a regular n-sided
polygon of side length s has a volume V = (1/3)*A*h and total surface area 
S = A + (1/2)*n*s*l where A is the base area and l the slant height, which may be 
calculated from the apothem of the base polygon, a = (1/2)*s*cot(pi/n) as 
A = (1/2)*n*s*a and l = sqrt(h^2 + a^2).
Use these formulas to define a function, pyramid_AV, returning V and S when passed
values for n, s and h.
"""

import math

def pyramid_AV(n:int, s:float, h:float):  # takes n, s and h, and returns V and S
    """ Return the volume and surface area of a pyramid with height h, and a base consisting of an n-sided polygon of side lenght s.
    """
    # Calculate the apothem
    apo = 0.5*s*(1/math.tan(math.pi/n))
    # Calculate the base area
    area_base = 0.5*n*s*apo
    # Calculate the slant height
    s_height = math.sqrt(h**2+apo**2)
    # Calculate the surface area
    surface_area = area_base + 0.5*n*s*s_height
    # Calculate the volume
    volume = (1/3)*area_base*h
    return surface_area, volume


number_sides = 4
side_length = 10
pyr_height = 5
area, vol = pyramid_AV(number_sides, side_length, pyr_height)
print(f"A pyramid with {number_sides} regular sides of length {side_length:.2f} and height {pyr_height:.2f} has \n Surface area: {area:.2f} u^2 \n Volume: {vol:.2f} u^3 ")