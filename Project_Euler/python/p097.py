
import os
import time

"""
The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 2^6972593 −1;
it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2^p −1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×2 ^ 27830457 +1.

Find the last ten digits of this prime number.
"""


if __name__ == '__main__':

    stime = time.time()

    value = 28433
    exp = 7830457

    for i in range(exp):
        value = 2*value % 10**10

    print("Prevent overflow Solution:{} Runtime:{}".format(value+1,time.time()-stime))

    stime = time.time()

    value = 28433
    exp = 7830457

    value = value * pow(2,exp,mod=10**10) % 10**10

    print("pow() Solution:{} Runtime:{}".format(value+1,time.time()-stime))
