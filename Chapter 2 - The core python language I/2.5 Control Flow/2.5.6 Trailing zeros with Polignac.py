"""
Write a Python program to determine f(n), the number of trailing zeros in n!,
using the special case of de Polignac’s formula:
                    f(n)=sum_(i=1) [n/5^i]
where [x] denotes the floor of x, the largest integer less than or equal to x.
"""

test = 10 # the n for which I want to know the trailing zeros of n!
for test in range(1,27):
    sum = 0
    i = 1
    while True:
        sum += int(test/5**i)
        i += 1
        if 5**i>test:
            break
    print("{:d}! has {:d} trailing zeros".format(test, sum))