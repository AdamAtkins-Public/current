import os
import math
import time

"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
"""

def median(a,b,c,d):
    return a+c,b+d

def count_medians(a,b,c,d,limit):
    medians = [(a,b),(c,d)]
    i = int(0)
    while i < len(medians)-1:
        while True:
            low = medians[i]
            high = medians[i+1]
            n,d = median(low[0],low[1],high[0],high[1])
            if not d > limit:
                medians.insert(i+1,(n,d))#stack
            else:
                break
        i+=1
    return len(medians)-2


if __name__ == '__main__':

    stime = time.time()

    count = count_medians(1,3,1,2,12000)

    print("Soltuion:{} Runtime:{}".format(count,time.time()-stime))

