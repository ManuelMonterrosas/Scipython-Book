"""
There is no exclusive-or operator provided “out of the box” by Python, but one
can be constructed from the existing operators. Devise two different ways of doing this.
The truth table for the xor operator is given in Table 2.9.
"""


# The function xor(a,b) should return True if only a or only b are True, and False otherwise
def xor1(a, b):
    return (a == True and b == False) or (a == False and b == True)


def xor2(a, b):
    return a+b == 1


print(xor1(True, False), xor1(True, True))
print(xor2(False, True), xor2(True, True))
