import os
import math
import time

"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

def return_signiture(value):
    copy = value.__str__()
    count = dict()
    signiture = ""
    for i in range(10):
        count[i.__str__()] = 0
    for digit in copy:
        count[digit.__str__()] += 1
    for i in range(10):
        signiture += count[i.__str__()].__str__() + "*"
    return signiture

def _val(value):
    sig = return_signiture(value)
    for i in range(2,7):
        if sig != return_signiture(value*i):
            break
    return sig == return_signiture(value*i) 

if __name__ == '__main__':
    
    stime = time.time()
    n = 1
    solution = None
    while(solution is None):
        for value in range(10**n, math.ceil((10**(n+1))/6)):
            if _val(value):
                solution = value
                break
        n+=1

    print("Solution:{} Runtime:{}".format(solution, time.time()-stime))
