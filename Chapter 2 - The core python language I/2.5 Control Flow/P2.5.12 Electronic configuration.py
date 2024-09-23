"""
The electron configuration of an atom is the specification of the distribution
of its electrons in atomic orbitals. An atomic orbital is identified by a principal quantum
number, n = 1, 2, 3, ... defining a shell comprised of one or more subshells defined
by the azimuthal quantum number, l = 0, 1, 2, ..., n-1. The values l = 0, 1, 2, 3 are
referred to be the letters s, p, d and f respectively. Thus, the first few orbitals are 1s
(n = 1; l = 0), 2s (n = 2; l = 0), 2p (n = 2; l = 1), 3s (n = 3; l = 0), and each shell has n
subshells. A maximum of 2*(2l + 1) electrons may occupy a given subshell.
According to the Madelung rule, the N electrons of an atom fill the orbitals in order
of increasing n + l such that whenever two orbitals have the same value of n + l, they
are filled in order of increasing n. For example, the ground state of titanium (N = 22) is
predicted (and found) to be 1s2,2s2,2p6,3s2,3p6,4s2,3d2.
Write a program to predict the electronic configurations of the elements up to rutherfordium
(N = 104). The output for titanium should be
Ti: 1s2.2s2.2p6.3s2.3p6.4s2.3d2
A Python list containing the element symbols in order may be downloaded from
https://scipython.com/ex/bbb.

As a bonus exercise, modify your program to output the configurations using the
convention that the part of the configuration corresponding to the outermost closed shell,
a noble gas configuration, is replaced by the noble gas symbol in square brackets; thus,
Ti: [Ar].4s2.3d2
the configuration of Argon being 1s2.2s2.2p6.3s2.3p6.
"""
from element_symbols import element_symbols

max_atomic_number = 104
l_letters = ['s', 'p', 'd', 'f']
result_matrix = []  # I want to store (atomic number, element symbol, configuration)
option = 2
noble_numbers = [2, 10, 18, 36, 54, 86]  # for output with noble gases
if option == 1:  # normal output
    for atomic_number in range(1, max_atomic_number+1):
        available = atomic_number
        configuration = []
        n = 1
        l = 0
        max_sum_nl = 1
        while available > 0:  # here comes the hard part
            max_subshell = 2*(2*l+1)
            subshell = min(available, max_subshell)  # decide how many come in the subshell, either all available or the max. for the subshell 
            configuration.append(str(n)+l_letters[l]+str(subshell))  # append to result
            available -= subshell  # substract the used electrons from the total
            # Now I need change n and l following Madelung rule. In order of increasing n+l, and increasing n. l is maximum n-1
            if l == 0:
                max_sum_nl += 1
                # and assign new n,l values when the max changed
                l = int((max_sum_nl-1)/2)
                n = max_sum_nl - l
            # If the max didn't change, just decrease l and increase n
            else:
                l -= 1
                n += 1
        configuration = '.'.join(configuration)
        result_matrix.append([atomic_number, element_symbols[atomic_number-1], configuration])
    # print(result_matrix[:,1])
    print('-'*27)
    for row in range(len(result_matrix)):
        print(result_matrix[row][0], '\t'+result_matrix[row][1], '\t'+result_matrix[row][2])
    print('-'*27)
if option == 2:  # output using noble gases
    for atomic_number in range(1, max_atomic_number+1):
        available = atomic_number
        configuration = []
        n = 1
        l = 0
        max_sum_nl = 1
        for i in range(len(noble_numbers)-1, -1, -1):
            if atomic_number > noble_numbers[i]:
                configuration = ["["+element_symbols[noble_numbers[i]-1]+"]"]
                n = i + 2
                l = 0
                max_sum_nl = n + l
                available -= noble_numbers[i]
                break
        while available > 0:  # here comes the hard part
            max_subshell = 2*(2*l+1)
            subshell = min(available, max_subshell)  # decide how many come in the subshell, either all available or the max. for the subshell 
            configuration.append(str(n)+l_letters[l]+str(subshell))  # append to result
            available -= subshell  # substract the used electrons from the total
            # Now I need change n and l following Madelung rule. In order of increasing n+l, and increasing n. l is maximum n-1
            if l == 0:
                max_sum_nl += 1
                # and assign new n,l values when the max changed
                l = int((max_sum_nl-1)/2)
                n = max_sum_nl - l
            # If the max didn't change, just decrease l and increase n
            else:
                l -= 1
                n += 1
        configuration = '.'.join(configuration)
        result_matrix.append([atomic_number, element_symbols[atomic_number-1], configuration])
    # print(result_matrix[:,1])
    print('-'*27)
    for row in range(len(result_matrix)):
        print(result_matrix[row][0], '\t'+result_matrix[row][1], '\t'+result_matrix[row][2])
    print('-'*27)