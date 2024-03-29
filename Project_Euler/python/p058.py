﻿
import os
import time

"""
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that
8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed.
If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""

def is_prime(n):
    if n == 2:
        return True
    if n & 1 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

def is_prime_6k(n):
    if n <= 3:
        return n > 1
    if n & 1 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

def add_layer(primes,nonprimes,layer,last_value):
    increase = 2 * layer
    for i in range(4):
        last_value += increase
        if is_prime_6k(last_value):
            primes += 1
        else:
            nonprimes += 1
    return primes, nonprimes, last_value

if __name__ == '__main__':
    stime = time.time()
    primes = int(3)
    nonprimes = int(1)
    layer = int(1)
    last_value = int(9)
    solution = None
    while(solution is None):
        layer += 1
        primes, nonprimes, last_value = add_layer(primes,nonprimes,layer,last_value)
        if primes/(primes+nonprimes+1) < 0.1:
            solution = (2*layer)+1
            break
    print("Solution:{} Runtime:{}".format(solution,time.time()-stime))


