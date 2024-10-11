""" Python follows the convention of many computer languages in choosing to
define 0^0 = 1. Write a function, powr(a, b), which behaves the same as the Python
expression a**b (or, for that matter, math.pow(a,b)) but raises a ValueError if a and b
are both zero.
"""

def powr(a:float, b:float):  # The types here are suggestions, if the user makes a mistake the program will not catch automatically
    "Return a^b. Return erorr for 0^0."
    assert type(a) in (float, int) and type(b) in (float, int), "Please use real numbers."  # asser error is better in that case
    if a == b == 0:
        raise ValueError('0^0 is not defined.')
    return a**b


# print(powr('k', 3))  # Returns error
for i in range(2):
    for j in range(2):
        print(f'{i}^{j} = {powr(i,j)}.')