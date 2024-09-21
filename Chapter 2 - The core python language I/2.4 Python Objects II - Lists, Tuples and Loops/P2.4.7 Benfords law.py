"""
Benford’s law is an observation about the distribution of the frequencies of the
first digits of the numbers in many different data sets. It is frequently found that the first
digits are not uniformly distributed, but follow the logarithmic distribution

                        P(d) = log10((d+1)/d)

That is, numbers starting with 1 are more common than those starting with 2, and so on,
with those starting with 9 the least common.

Benford’s law is most accurate for data sets which span several orders of magnitude,
and can be proved to be exact for some infinite sequences of numbers.
(a) Demonstrate that the first digits of the first 500 Fibonacci numbers (see Example
E2.20) follow Benford’s law quite closely.
(b) The length of the amino acid sequences of 500 randomly chosen proteins
are provided in the file protein_lengths.py which can be downloaded from
https://scipython.com/ex/bba. This file contains a list, naa, which can be imported
at the start of your program with
from protein_lengths import naa
To what extent does the distribution of protein lengths obey Benford’s law?
"""

import numpy as np
option = 4 # 1 and 2 are unsuccesful attempts of mine (memory problems). 3 is the book solution
# takeaway: efficiency matters. I don't need to store all the fibonacci numbers if I just care about the first digit
# also, not everything needs to be linear. In the same step I can calculate a number and take its first digit.
if option == 1:
    ### Recursive definition. It works fine but my old laptop cannot compute more than 50 without crashing. Try a read-write function so that all steps are equally
    # def fibonacci(n):  # calculates the nth fibonacci number (sum of previous two number, with the first two being 1)
    #     if n>2:
    #         return fibonacci(n-1) + fibonacci(n-2)
    #     else:
    #         return 1

    # stop_n = 10  # fibonacci numbers to calculate
    # frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # to store digit frequency
    # for i in range(1, stop_n):  # for the first n fibonacci numbers
    #     first_digit = str(fibonacci(i))[0]  # get their first digit
    #     frequency[int(first_digit)-1] += 1  # and store their frequency
    # for i in range(len(frequency)):
    #     frequency[i] = frequency[i]/stop_n  # then normalize by n to get probability
    # print(frequency)
    pass

if option == 2:
    ### Read-write function. If nth number exists in a file read it, otherwise calculate it
    # this works for a while, but gets memory-overflow around step 45 in my computer. then gives negative values.
    def fibonacci(n):  # calculates the nth fibonacci number (sum of previous two number, with the first two being 1)
        # check if the nth fibonacci number is already in the file
        fibo_file = r'C:\Users\manym\Documents\Coding\Scipython-book\Chapter 2 - The core python language I\2.4 Python Objects II - Lists, Tuples and Loops\Fibonacci_list.csv'
        fibo_numbers = np.loadtxt(fibo_file, delimiter=',', dtype=int)
        if n in fibo_numbers[:,0]: # if the number is already there, read it
            return fibo_numbers[n-1,1]
        else:
            for i in range(np.max(fibo_numbers[:,0])+1, n+1):
                new_fibo = fibo_numbers[i-2,1]+fibo_numbers[i-3,1]
                fibo_numbers = np.append(fibo_numbers, [[i, new_fibo]], axis=0)
            np.savetxt(fibo_file, fibo_numbers, delimiter=',', fmt='%d')
            return fibo_numbers[n-1,1] # if the number is not there calculate all the missing numbers until the nth and write them
        
    # print(fibonacci(44))
    pass

if option == 3: # a. Benford's Law matches pretty well here
    ### Now I am trying book solution. Maybe it is more efficient since it just needs to remember two fibonacci numbers at the same time
    import math

    # We will analyse the first n Fibonacci numbers
    n = 500
    # The first 2 numbers of the series are 1, 1
    a = b = 1
    # fd is a list such that fd[d] is the number of Fibonacci numbers up to n
    # which start with the digit d. Note that none start with 0!
    fd = [None,2,0,0,0,0,0,0,0,0]

    # Loop over the 3rd, 4th, ..., nth Fibonacci numbers
    for i in range(3,n+1):
        # This is the propagation step: generate the current Fibonacci number, a,
        # as the sum of the last two numbers (a+b), and store the old value of a
        # as b (the old value of b is forgotten).
        a, b = a+b, a
        # The first digit of a
        d = int(a/10**(int(math.log10(a))))
        fd[d] += 1

    # The digits 1,2,3,4,5,6,7,8,9
    digits = range(1,10)
    benford = [None]
    for d in digits:
        # Normalize fd by dividing by n so it represents a probability
        fd[d] /= n
        # Use Benford's Law to predict the frequency of first digit d
        benford.append(math.log10((d+1)/d))

    # Output a table of the predicted and observed distribution of first digits
    print('-'*27)
    print('Digit  Predicted   Observed')
    print('-'*27)
    for d in digits:
        print('  {:1d}       {:5.3f}      {:5.3f}'.format(d, benford[d], fd[d]))
    print('-'*27)

if option == 4: # b. Benford's Law is less accurate here. Is our dataset not big enough?
    from protein_lengths import naa
    import math

    fd = [None,0,0,0,0,0,0,0,0,0]
    n=len(naa)
    for i in range(n):
        a = naa[i]
        d = int(a/10**(int(math.log10(a))))
        fd[d] += 1

    digits = range(1,10)
    benford = [None]
    for d in digits:
        # Normalize fd by dividing by n so it represents a probability
        fd[d] /= n
        # Use Benford's Law to predict the frequency of first digit d
        benford.append(math.log10((d+1)/d))

    # Output a table of the predicted and observed distribution of first digits
    print('-'*27)
    print('Digit  Predicted   Observed')
    print('-'*27)
    for d in digits:
        print('  {:1d}       {:5.3f}      {:5.3f}'.format(d, benford[d], fd[d]))
    print('-'*27)
    pass