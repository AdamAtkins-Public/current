
import os
import math

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def gather_factors(n):
    factors = list()
    n_half = math.ceil(n/2)
    while n_half > 1:
        d = math.gcd(n_half, n)
        if d != 1 :
            factors.append(d)
            n = int(n/d)
            n_half = int(n_half/d)
        else:
            n_half = n_half - 1 
    if n != 1:
        factors.append(n)
    return factors



if __name__ == "__main__":
    n = 13195
    print(gather_factors(n))
    n = 600851475143
    print(gather_factors(n))
