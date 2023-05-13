import os
import time


"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
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

#sort O(nlogn)
def is_permutation(a,b):
    a_ = a.__str__()
    b_ = b.__str__()
    valid = False
    if len(a_) == len(b_):
        a_ = sorted(a_)
        b_ = sorted(b_)
        valid = True
        for i in range(len(a_)):
            if not a_[i] == b_[i]:
                valid = False
                break
    return valid

#map O(n)
def is_permutation_(a,b):
    a_string = a.__str__()
    b_string = b.__str__()

    if len(a_string) != len(b_string):
        return False

    digit_map = dict(zip(range(0,10),[0]*10))

    for digit in a_string:
        digit_map[int(digit)] += 1

    for digit in b_string:
        digit_map[int(digit)] -= 1
        if digit_map[int(digit)] < 0:
            return False

    return True

if __name__ == '__main__':

    stime = time.time()

    #brute force
    min = float('inf')
    for i in range((10**7)-1,1,-2):
        #upper bound
        if i/(i-1) > min:
           break
        p_n = euler_totient(i)
        value = i/p_n
        if value < min and is_permutation_(i,p_n):
            min = value
            min_n = i

    print("Solution:{} Runtime:{}".format(min_n,time.time()-stime))
#8319823

