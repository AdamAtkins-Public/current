import os
import math
import time

"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
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

def max_prime(primes):
    return max(list(primes))

def insert_next_prime(primes):
    n = max_prime(primes)
    while(True):
        n += 2
        if is_prime(n):
            primes[n] = len(primes) + 1
            break

def conjecture(prime,n):
    return prime + 2*n**2

if __name__ == '__main__':
    stime = time.time()
    primes = {2:1, 3:2}
    composite = 5
    falsified_composite = None
    while(True):
        if composite > max_prime(primes):
            insert_next_prime(primes)
        elif composite in primes:
            composite += 2
        else:
            for prime in list(primes)[-2::-1]:
                n = 1
                while(conjecture(prime,n) < composite):
                    n += 1
                if conjecture(prime,n) == composite:
                    composite += 2
                    break
                else:
                    if prime == 2:
                        falsified_composite = composite
                        break
                    continue
        if falsified_composite is not None:
            break
    print("Solution: {0}\nRuntime: {1}".format(falsified_composite,time.time()-stime))    
