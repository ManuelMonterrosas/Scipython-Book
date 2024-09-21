"""
The Hamming distance between two equal-length strings is the number of
positions at which the characters are different. Write a Python routine to calculate the
Hamming distance between two strings, s1 and s2.
"""

def hamming(s1, s2):
    count = 0
    for i in range(len(s1)):  # assuming s1 and s2 are the same length
        if s1[i] != s2[i]:
            count += 1
    return count

a = 'abcd'
b = 'aaaa'
print(hamming(a, b))