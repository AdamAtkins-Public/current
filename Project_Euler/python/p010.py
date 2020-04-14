
import os
import math

'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

#prime sieve
def collect_primes(n):
    primes = list()
    primes.append(2)
    i = int(3)
    while i < n:
        composite = False
        for j in range(len(primes)):
            if primes[j] > math.sqrt(i):
                break
            if i % primes[j] == 0:
                composite = True
                break
        if not composite:
            primes.append(i)
        i = i + 2
    return primes

if __name__ == '__main__':
    n = 2000000
    primes = collect_primes(n)
    #Sum primes
    sum = 0
    for i in range(len(primes)):
        sum = sum + primes[i]
    print(sum)
