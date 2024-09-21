"""
The Luhn algorithm is a simple checksum formula used to validate credit card
and bank account numbers. It is designed to prevent common errors in transcribing the
number, and detects all single-digit errors and almost all transpositions of two adjacent
digits. The algorithm may be written as the following steps:

1. Reverse the number.
2. Treating the number as an array of digits, take the even-indexed digits (where the
indexes start at 1) and double their values. If a doubled digit results in a number
greater than 10, add the two digits (e.g. the digit 6 becomes 12 and hence 1 + 2 =
3).
3. Sum this modified array.
4. If the sum of the array modulo 10 is 0 the credit card number is valid.

Write a Python program to take a credit card number as a string of digits (possibly in
groups, separated by spaces) and establish if it is valid or not. For example, the string
'4799 2739 8713 6272' is a valid credit card number, but any number with a single
digit in this string changed is not.
"""

test = '4799 2739 8713 6272'
to_check = test[::-1].replace(' ', '')  # reverse number and get rid of white spaces
to_check = list(to_check)
sumdigits = 0
for i in range(1, len(to_check)+1):
    if i%2==0: # double the values of the even-index digits. If the double value is larger than 10, add the two digits
        double_value = int(to_check[i-1])*2
        if double_value > 9:
            double_value = 1 + double_value%10
        to_check[i-1] = str(double_value)
    sumdigits += int(to_check[i-1])

if sumdigits%10==0:
    print(test, 'is a valid credit card number.')
else:
    print(test, 'is not a valid credit card number.')

# to_check = ''.join(to_check)
# print(to_check)
