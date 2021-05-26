import os
import time

"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
n 	Relatively Prime 	φ(n) 	n/φ(n)
2 	1 	1 	2
3 	1,2 	2 	1.5
4 	1,3 	2 	2
5 	1,2,3,4 	4 	1.25
6 	1,5 	2 	3
7 	1,2,3,4,5,6 	6 	1.1666...
8 	1,3,5,7 	4 	2
9 	1,2,4,5,7,8 	6 	1.5
10 	1,3,7,9 	4 	2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""

#from wikipedia
def trial_division(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n /= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n /= f
        else:
            f += 2
    if n != 1: a.append(n)
    return a

def euler_totient(n):
    pf = trial_division(n)#sieve primes to limit
    pf_set = set(pf)
    tuples = []
    product = int(1) 
    for f in pf_set:
        tuples.append((f,pf.count(f)))#optimize count knowing pf asc sorted
    for t in tuples:
        product *= pow(t[0],t[1]-1)*(t[0]-1)
    return int(product)

if __name__ == '__main__':

    stime = time.time()

    max = float('-inf')
    for i in range(2,1000001):
        value = i/euler_totient(i)
        if value > max:
            max = value
            max_n = i

    print("Solution:{} Runtime:{}".format(max_n,time.time()-stime))
