"""
A Gaussian integer is a complex number whose real and imaginary parts are
both integers. A Gaussian prime is a Gaussian integer x + iy such that either:
    * one of x and y is zero and the other is a prime number of the form 4n + 3 or
      -(4n + 3) for some integer n >= 0; or
    * both x and y are nonzero and x^2 + y^2 is prime.
Consider the sequence of Gaussian integers traced out by an imaginary particle,
initially at c_0, moving in the complex plane according to the following rule: it takes
integer steps in its current direction (+-1 in either the real or imaginary direction), 
but turns left if it encounters a Gaussian prime. Its initial direction is in the positive 
real direction (delta c = 1 + 0i ) => delta x = 1; delta y = 0). The path traced out by
the particle is called a Gaussian prime spiral.
Write a program to plot the Gaussian prime spiral starting at c0 = 5 + 23i.
"""

import numpy as np
import matplotlib.pyplot as plt

def is_prime(number:int):
    """ Returns True if the number is prime or False otherwise
    """
    if number == 0 or number == 1:  # by definition, these are not prime numbers
        return False
    if number == 2 or number == 3:  # the smallest primes, I need  to include them separately
        return True
    for i in range(2,int(np.sqrt(number)+1)): # we only need to test dividers up to sqrt(n)
        if number % i == 0:
            return False
    return True

def is_gaussprime(number:complex):
    """ Returns True if the number is a Gauss prime or False otherwise
    """
    x = number.real
    y = number.imag
    if x == 0 and is_prime(np.abs(y)) and np.abs(y)%4 == 3:
        return True
    elif y == 0 and is_prime(np.abs(x)) and np.abs(x)%4 == 3:
        return True
    elif is_prime(x**2 + y**2):
        return True
    return False

def move_forward(number:complex, direction:str):
    """ Returns a complex number that is the next step in the given direction.
    """
    x = number.real
    y = number.imag
    if direction == '+x':
        return complex(x+1, y)
    if direction == '+y':
        return complex(x, y+1)
    if direction == '-x':
        return complex(x-1, y)
    if direction == '-y':
        return complex(x, y-1)

# initialize conditions    
init_pos = 5 + 23j  # init_pos.real = 5, init_pos.imag = 23
direction_list = ['+x', '+y', '-x', '-y']  # all the posible directions
direction_counter = 0  # I need this to keep track of the direction order
step = 0
max_step = 10000
x = []  # just an array with all the x positions
y = []  # just an array with all the y positions
pos = init_pos  # the starting position
direction = direction_list[direction_counter]  # the starting direction

# Main loop of game
while step <= max_step:
    # save the position of this step
    x = np.append(x, pos.real)
    y = np.append(y, pos.imag) 
    # take steps in the current direction, turn left if you encounter a gaussian prime
    pos = move_forward(pos, direction)
    if is_gaussprime(pos):
        direction_counter += 1
        direction = direction_list[direction_counter%4]
    step += 1

# Show the trajectory
plt.plot(x, y)
plt.show()