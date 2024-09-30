"""
The range of a projectile launched at an angle alpha and speed v on flat terrain is
            R = v^2*sin(2*alpha)/g
where g is the acceleration due to gravity, which may be taken to be 9.81 m/s^2 for
Earth. The maximum height attained by the projectile is given by
            H = v^2*sin^2(alpha)/(2*g)
(We neglect air resistance and the curvature and rotation of the Earth.) 
Write a function to calculate and return the range and maximum height of a projectile, 
taking alpha and v as arguments. Test it with the values v = 10 m/s and alpha = 30°.
"""

import math

def projectile_rh(alpha:float, v:float):
    """ Return the range and maximum height of a projectile when given the launch angle and initial speed
    """
    g = 9.81  # m/s^2
    pro_range = v**2*math.sin(2*math.radians(alpha))/g  # we assume that alpha is given in rads
    pro_height = v**2*(math.sin(math.radians(alpha)))**2/(2*g)
    return pro_range, pro_height

test_speed = 10  # m/s
test_angle = 30  # degs
test_range, test_height = projectile_rh(test_angle, test_speed)
print(f"The projectile has the range {test_range:.2f} m and maximum height {test_height:.2f} m")