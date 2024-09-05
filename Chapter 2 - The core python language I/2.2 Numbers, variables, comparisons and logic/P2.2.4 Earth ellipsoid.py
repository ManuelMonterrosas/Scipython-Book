"""
The World Geodetic System is a set of international standards for describing
the shape of the Earth. In the latest WGS-84 revision, the Earth’s geoid is approximated
to a reference ellipsoid that takes the form of an oblate spheroid with semi-major and
semi-minor axes a = 6,378,137.0 m and c = 6,356,752.314245 m respectively.
Use the formula for the surface area of an oblate spheroid, to calculate the surface area
of this reference ellipsoid and compare it with the surface area of the Earth assumed to
be a sphere with radius 6371 km.
(the formula is given in the book)
"""
import math


# Formula for area of an oblate spheroid
def area_oblate(a, c):
    e = math.sqrt(1 - c**2/a**2)
    area = 2*math.pi*a**2*(1+((1-e**2)/e)*math.atanh(e))
    return area


# Formula for area of an oblate spheroid
def area_sphere(r):
    area = 4*math.pi*r**2
    return area


oblate = area_oblate(6378137.0, 6356752.314245)
sphere = area_sphere(6371000)
print(oblate)
print(sphere)
# less than 0.00023% error
print(100*(oblate-sphere)/((oblate+sphere)/2))
