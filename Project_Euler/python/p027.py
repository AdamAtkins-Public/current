import os
import time

"""
Euler discovered the remarkable quadratic formula:
n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 \le n \le 39.
However, when
n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41,
and certainly when
n = 41, 41^2 + 41 + 41
is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601
was discovered, which produces 80 primes for the consecutive values 0 \le n \le 79. 

The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
n^2 + an + b, where |a| < 1000 and |b| \le 1000 

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b,
for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""

def is_prime(n):
    if n == 2:
        return True
    elif n < 2:
        return False
    if n & 1 == 0:
        return False
    for i in range(3,int(n**0.5),2):
        if n % i == 0:
            return False
    return True

def quadratic(n,a,b):
    return n**2 + a*n + b

def brute_force():
    primes = {}
    max_count = (int(-1),int(),int())
    count = 0
    for a in range(-999,1000):
        for b in range(-1000,1001):
            n = 0
            while(True):
                number = quadratic(n,a,b)
                if number not in primes:
                    if is_prime(number): primes[number] = 1
                if number in primes:
                    if n > max_count[0]: max_count = (n,a,b)
                    n += 1
                else:
                    break
    return max_count

if __name__ == '__main__':

    stime = time.time()
    max_count = brute_force()
    print("Solution: {0}\nRuntime: {1}".format(max_count[1]*max_count[2],time.time()-stime))
