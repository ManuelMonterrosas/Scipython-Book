""" Adapt the function of Example E4.3, which returns a vector in the following
form:
>>> print(str_vector([-2, 3.5]))
-2i + 3.5j
>>> print(str_vector((4, 0.5, -2)))
4i + 0.5j - 2k
to raise an exception if any element in the vector array does not represent a real number.
"""

def str_vector(vec_list):
    """ Return the vector representation using i,j,k of a 2D- or 3D-vector given as a list or tuple.
    """
    unit_vectors = ['i', 'j', 'k']
    result = []
    try:
        assert len(vec_list) in (2,3)
        for i, component in enumerate(vec_list):
            result.append('{}{}'.format(float(component), unit_vectors[i]))
    except AssertionError:
        return f'Handled error: {vec_list} is not 2D or 3D.'
    except ValueError:
        return f'Handled error: {component} is not a real number.'
    except TypeError:
        return f'Handled error: {vec_list} is not a list/tuple.'
    return ' + '.join(result).replace('+ -', '-')

vec0 = [3]  # a nicely defined 1D vector
vec1 = [3, -1, 7]  # a nicely defined 2D vector
vec2 = [-4, 21, "-10"]  # a nicely defined 3D vector
vec3 = ["8", 4, -5, 40]  # a 4D vector
vec4 = ["a", "b", "c"]  # not a real vector
vec5 = 123  # this is not even a list/tuple
vecs = [vec0, vec1, vec2, vec3, vec4, vec5]  # with this vector I test for interesting errors
for vec in vecs:
    print(str_vector(vec))
