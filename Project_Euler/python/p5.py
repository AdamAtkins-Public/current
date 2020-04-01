
import os
import math

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def recursive_prime_factor(n):
    factors = list()
    a = 2
    recurred = False
    while a < n:
        d = math.gcd(a,n)
        if d != 1:
            n = math.floor(n/d)
            factors.extend(recursive_prime_factor(n))
            factors.extend(recursive_prime_factor(d))
            recurred = True
            break
        a = a + 1
    if n != 1 and not recurred:
        factors.append(n)
    factors.sort()
    return factors


if __name__ == '__main__':
    n = int(2520)
    factors = recursive_prime_factor(n)
    print(factors)

    max = 20
    i = int(2)
    min_collection = list()
    while i < max:
        factors = recursive_prime_factor(i)
        for k in range(len(factors)):
            new_count = factors.count(factors[k])
            old_count = min_collection.count(factors[k])
            if new_count > old_count:
                while old_count < new_count:
                    min_collection.append(factors[k])
                    old_count = old_count + 1
        i = i +1

    min_collection.sort()
    print(min_collection)
    product = int(1)
    for j in range(len(min_collection)):
        product = product * min_collection[j]

    print(product)

