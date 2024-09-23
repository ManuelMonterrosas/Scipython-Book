"""
Write a program to find the smallest positive integer, n, whose factorial is not
divisible by the sum of its digits. For example, 6 is not such a number because 6! = 720
and 7 + 2 + 0 = 9 divides 720.
"""

import math

def fact(n: int):
    "Return n!"
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

def fact_div_sum(n:int):
    "Return True if n! is divisible by the sum of the digits of n!, or False otherwise."
    # Calculate the sum of the digits of n!
    factorial = str(fact(n))
    sum = 0
    for i in range(len(factorial)):
        sum += int(factorial[i])
    if int(factorial) % sum == 0:  # this means it is divisible
        return True
    else:
        return False

current_number = 1  # current number to evaluate, changes in the while loop
max_iterations = 500  # in case there is no solution, could be a tricky question
flag = True  # will turn False if we find n such that n! is NOT divisible by the sum of the digits in n!
while flag and current_number<=max_iterations:
    if not fact_div_sum(current_number):
        print('{}! is not divisible by the sum of its digits.'.format(current_number))
        print('{}! = {}'.format(current_number, fact(current_number)))
        flag = False
    if current_number == max_iterations:
        print("I have reached the maximum number of iterations.")
    current_number += 1
