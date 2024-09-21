"""
The algorithm known as the Sieve of Eratosthenes finds the prime numbers
in a list 2, 3, ..., n. It may be summarized as follows, starting at p = 2, the first prime
number:
Step 1. Mark all the multiples of p in the list as non-prime (that is, the numbers mp
where m = 2, 3, 4,... these numbers are composite.
Step 2. Find the first unmarked number greater than p in the list. If there is no such
number, stop.
Step 3. Let p equal this new number and return to Step 1.
When the algorithm stops, the unmarked numbers are the primes.
Implement the Sieve of Eratosthenes in a Python program and find all the primes
under 10 000.
"""

n_max = 10000  # maximum number to test for primes
current_p = 2  # current prime
list_to_test = list(range(2, n_max+1))  # list to test
while True:  # repeat while there are still primes
    current_index = list_to_test.index(current_p)
    if current_index == len(list_to_test)-1:  # I have reached the end
        break
    for i in range(len(list_to_test)-1, current_index, -1):  # remove the multiples of the current prime number
        if list_to_test[i]%current_p == 0:
            list_to_test.pop(i)
    # jump to the next prime
    current_p = list_to_test[current_index+1]

print(list_to_test)