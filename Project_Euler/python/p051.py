import os
import numpy as np
import itertools
import time

"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""

def generalize(value):
    copy = value.__str__()
    G = dict()
    query = str()
    queries = list()
    for i in range(4):
        G[i] = list()
    for digit in range(len(copy)-1):
        if int(copy[digit]) < 4:
            G[int(copy[digit])].append(digit)
    for i in range(4):
        if len(G[i]) > 2:#
            query = build_generalization(G[i],copy)
            queries.append(query)
    return queries

#reduce string operations for speedup
def build_generalization(digit_indexes,value):
    copy = value.__str__()
    solution = ""
    prev_j = -1
    for j in digit_indexes:
        solution += copy[prev_j+1:j] + "*"
        prev_j = j
    solution += copy[prev_j+1:]
    return solution

def replace_generalization(gen,value):
    copy = gen.__str__()
    solution = ""
    prev_d = -1
    for digit in range(len(copy)-1):
        if copy[digit] == "*":
            solution += copy[prev_d+1:digit] + value.__str__()
            prev_d = digit
    solution += copy[prev_d+1:]
    return solution

def primes_search(primes):
    for p in sorted(list(primes)):
        queries = generalize(p)
        for q in queries:
            if solution_found(q,primes):#referential copy of dict
                return p
    return None

def solution_found(query,primes):
    min = int(0)
    q = str()
    count = int(0)
    if query[0] == "*":
        min = 1
    for i in range(min,10):
        q = replace_generalization(query,i)
        if int(q) in primes:
            count += 1
        if (8 - count) > (10 - i):
            return False
    if count > 7:
        return True
    return False

#implementation sieve of Eratothenes with numpy arrays, returns python dict with primes as keys
def erato_sieve(max):
    primes = np.ones(max+1,dtype=int)
    primes[0] = 0
    primes[1] = 0
    index = 2
    while index < max**0.5:
        if primes[index] == 1:
            k = index*index
            while k <= max:
                primes[k] = 0
                k += index
        index += 1
    primes = np.flatnonzero(primes)
    return dict(itertools.zip_longest(primes,[]))

if __name__ == '__main__':
    stime = time.time()
    n = 6
    solution = None
    while solution is None:
        max = "9"*(n)
        primes = erato_sieve(int(max))
        solution = primes_search(primes)
        n += 1
    print("Solution:{} Runtime:{}".format(solution, time.time()-stime))
