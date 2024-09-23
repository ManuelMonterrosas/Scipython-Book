"""
Euler’s totient function, phi(n), counts the number of positive integers less than
or equal to n that are relatively prime to n. (Two numbers, a and b, are relatively prime
if the only positive integer that divides both of them is 1; that is, if gcd(a, b) = 1.)
Write a Python program to compute phi(n) for 1 <= n < 100.
(Hint: you could use Euclid’s algorithm for the greatest common divisor given in the
example to Section 2.5.2.)
"""

def gcd(a, b):  # returns greatest common divider of a and b
    while b:
        a, b = b, a%b
    return a

n_max = 99
i = 1
totient = []
while True:
    if i > n_max:
        break
    count = 0
    for j in range(1, i+1):
        if gcd(j, i) == 1:
            count += 1
    totient.append(count)
    i += 1
print(totient)