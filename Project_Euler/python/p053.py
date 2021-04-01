
import os
import time

"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5 choose 3 = 10

It is not until n = 23, that a value exceeds one-million: 23 choose 10 = 1144066

How many, not necessarily distinct, values of n choose r, for 1 <= n <= 100,
are greater than one-million?
"""

#The following solution uses Pascal's Triangle
# to count the coefficients that are greater than 1 million
if __name__ == '__main__':
    stime = time.time()
    prev_row = [1]
    count = int(0)
    for n in range(1,101):
        row = prev_row.copy()
        row.append(1)
        for i in range(1,len(prev_row)):
            row[i] = prev_row[i] + prev_row[i-1]
            if row[i] > 1000000:
                count += 1
        prev_row = row.copy()
    print("Solution:{} Runtime:{}".format(count, time.time()-stime))
