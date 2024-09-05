"""
Given a string representing a base-pair sequence (i.e. containing only the letters
A, G, C and T), determine the fraction of G and C bases in the sequence.
(Hint: strings have a count method, returning the number of occurrences of a
substring.)
(b) Using only string methods, devise a way to determine if a nucleotide sequence
is a palindrome in the sense that it is equal to its own complementary sequence
read backward. For example, the sequence TGGATCCA is palindromic because
its complement is ACCTAGGT, which is the same as the original sequence backward.
The complementary base pairs are (A, T) and (C, G).
"""

example = 'AGCTACGACAGTAGCTAGCTGATGCA'
fraction_G = example.count('G')/len(example)
fraction_C = example.count('C')/len(example)
print(fraction_G)
print(fraction_C)


# this function should return True if the input equals its reversed complement.
def is_palindromic(sequence):
    map_table = str.maketrans('ATCG', 'TAGC')
    return sequence[::-1] == sequence.translate(map_table)


example2 = 'TGGATCCA'
example3 = 'TGGATCCAA'
print(is_palindromic(example2))
print(is_palindromic(example3))
