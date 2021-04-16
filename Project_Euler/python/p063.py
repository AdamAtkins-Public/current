import os
import time

"""
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

if __name__ == '__main__':
    stime = time.time()
    count = int(0)
    for b in range(1,22):
        for a in range(1,10):
            if len(int(a**b).__str__()) == b:
                count += 1
            elif len(int(a**b).__str__())>b:
                break
    print("solution:{} Runtime:{}".format(count, time.time()-stime))
