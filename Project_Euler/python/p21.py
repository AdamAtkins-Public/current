
import os
import time
import p12 #list_factors(n)

'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

def d(n):
    return sum(p12.list_factors(n)[:-1])

amicable_dict = dict()
amicable_pairs = list()

def amicable_pairs_f(n):

    #d(a) = b
    b = amicable_dict.get(n)
    if b is None:
        b = d(n)
        amicable_dict[n] = b

    #d(b) = d(b)
    d_b = amicable_dict.get(b)
    if d_b is None:
       d_b = d(b) 
       amicable_dict[b] = d_b

    if d_b == n and n != b:
        amicable_pairs.append((n,b))

    return b


if __name__ == '__main__':
    s_time = time.time()
    for n in range(1,10000):
        amicable_pairs_f(n)
    
    sum = int(0)
    for pair in range(0,len(amicable_pairs),2):
        sum += amicable_pairs[pair][0] + amicable_pairs[pair][1]
    print(sum)
    print(time.time()-s_time)