
import os
import math

"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

def is_prime(n):
    if n == 2:
        return True
    elif n < 2:
        return False
    if n & 1 == 0:
        return False
    for i in range(2, math.ceil(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def is_circular_prime(n):
    num_str = str(n)
    if not is_prime(int(num_str)):
        return False
    if len(num_str) > 1:
        for i in range(len(num_str)):
            old_num_str = num_str
            num_str = old_num_str[1:] + num_str[0]
            if not is_prime(int(num_str)):
                return False
    return True


if __name__ == '__main__':
    target = 1000000
    circular_primes = []
    for i in range(target):
        if is_circular_prime(i):
            circular_primes.append(i)
    print(len(circular_primes))

