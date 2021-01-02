import os
import time

"""
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
"""

if __name__ == '__main__':
    stime = time.time()
    sum = 0
    for i in range(1,1001):
        sum += i**i
    print("Solution: {0}\nRuntime: {1}".format(str(sum)[-10:],time.time()-stime))
