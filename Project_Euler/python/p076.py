import os
import time

"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""

def partition_function(counts,N):
    if N < 0:
        return 0
    return counts[N]

def pfs_(counts,N):
    gp = generalized_pentagonal()
    sign = 1
    total = int(0)
    previous_total = total#loop control
    while True:
        total = total + sign*partition_function(counts,N-gp.__next__())#can modify partition_function to throw
        total = total + sign*partition_function(counts,N-gp.__next__())
        if previous_total == total:
            break
        previous_total = total
        sign *= -1
    counts[N] = total
    return total


def generalized_pentagonal():
    k = 1
    while True:
        yield k*((3*k)-1)//2
        if k > 0:
            k *= -1
        else:
            k *= -1
            k += 1

if __name__ == '__main__':

    stime = time.time()

    counts = {0:1,1:1,2:2}
    for i in range(3,101):
        pfs_(counts,i)

    print("Solution:{} Runtime:{}".format(counts[100]-1,time.time()-stime))
