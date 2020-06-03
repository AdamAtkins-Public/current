
import os
import math

"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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

def retract(n):
    #from left
    for i in range(1,len(str(n))):
        if not is_prime(int(str(n)[i:])):
            return False
    #from right
    for i in range(1,len(str(n))):
        if not is_prime(int(str(n)[0:-i])):
            return False
    return True

if __name__ == '__main__':
    primes = []
    number = int(11)
    while len(primes) < 11:
        if is_prime(number):
            if retract(number):
                primes.append(number)
        number += 2
    print(sum(number for number in primes))
