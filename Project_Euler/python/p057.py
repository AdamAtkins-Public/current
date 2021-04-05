import os
import time

"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
"""

if __name__ == '__main__':
    stime = time.time()
    count = int(0)
    numerator = int(1)
    denominator = int(2)
    new_denominator = int(0)
    check_numerator = int(0)
    for i in range(1000):
        check_numerator = denominator + numerator
        if len(check_numerator.__str__()) > len(denominator.__str__()):
            count += 1
        #iterate
        new_denominator = 2*denominator + numerator
        numerator = denominator
        denominator = new_denominator

    print("Solution:{} Runtime:{}".format(count, time.time() - stime))
