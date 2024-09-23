"""
Write two functions which, given two lists of length 3 representing threedimensional
vectors a and b, calculate the dot product, a dot b and the vector (cross)
product, a x b.
Write two more functions to return the scalar triple product, a dot (b x c) and the vector
triple product, a x (b x c).
"""

def dot_product(vec_a: list, vec_b: list) -> float:
    "Returns the dot product a (dot) b when given the two 3d vectors a and b."
    sum = 0
    for i in range(3):
        sum += vec_a[i]*vec_b[i]
    return sum

def cross_product(vec_a: list, vec_b: list) -> list:
    "Return the cross product a x b when given the two 3d vectors a and b."
    # I am defining the cross product manually. A loop would be more practical but I don't want to derive the formula now
    cross_x = vec_a[1]*vec_b[2]-vec_a[2]*vec_b[1]
    cross_y = vec_a[0]*vec_b[2]-vec_a[2]*vec_b[0]
    cross_z = vec_a[0]*vec_b[1]-vec_a[1]*vec_b[0]
    return [cross_x, -cross_y, cross_z]

def scalar_triple(vec_a: list, vec_b: list, vec_c: list) -> float:
    return dot_product(vec_a, cross_product(vec_b, vec_c))

def vector_triple(vec_a: list, vec_b: list, vec_c: list) -> list:
    return cross_product(vec_a, cross_product(vec_b, vec_c))

a = [3, 2, 6]
b = [2, 1, 4]
c = [1, 2, 3]

print(dot_product(a,b))
print(cross_product(a,b))
print(scalar_triple(a, b, c))
print(vector_triple(a, b, c))