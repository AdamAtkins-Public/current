import os
import math
import time

"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""

def is_prime(n):
    if n == 2:
        return True
    elif n < 2:
        return False
    if n & 1 == 0:
        return False
    for i in range(3, math.ceil(math.sqrt(n)+1), 2):
        if n % i == 0:
            return False
    return True

def prime_factorization(n, primes):
    factorization = []
    for prime in primes:
        factor = (prime,int(0))
        while n > 1 and n % prime == 0:
            n = n / prime
            factor = (prime,factor[1]+1)
        if factor[1] > 0:
            factorization.append(factor)
        if n == 1:
            break
    return factorization



if __name__ == '__main__':
    stime = time.time()
    primes = []
    consecutive = []
    number = 2
    while(True):
        if is_prime(number):
            primes.append(number)
            consecutive.clear()
        elif len(prime_factorization(number,primes)) == 4:
            consecutive.append(number)
        else:
            consecutive.clear()
        if len(consecutive) > 3:
            break
        number += 1
    print("Solution: {0}\nRuntime: {1}".format(consecutive[0],time.time()-stime))
