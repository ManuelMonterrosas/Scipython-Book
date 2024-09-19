"""
Write a short Python program which, given an array of integers, a, calculates
an array of the same length, p, in which p[i] is the product of all the integers in a except
a[i]. So, for example, if a = [1, 2, 3], then p is [6, 3, 2].
"""

a = [1, 2, 3]
# This could also be done in a function
p = []
for i in range(len(a)):
    product = 1
    for k in range(len(a)):
        if k != i:
            product = product * a[k]    
    p.append(product)
print(p)