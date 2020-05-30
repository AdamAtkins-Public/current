
import os
import math
import time

"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly
believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing 
two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

def is_curious_fraction(num, denom):
    num_str = str(num)
    denom_str = str(denom)
    for char in num_str:
        #trivial
        if char == '0':
            continue
        if char in denom_str:
            num_reduced = num_str.replace(char,'',1)
            denom_reduced = denom_str.replace(char,'',1)
            if int(denom_reduced) != 0:
                if num/denom == int(num_reduced)/int(denom_reduced):
                    return True




if __name__ == '__main__':

    stime = time.time()

    #collect nontrivial curious fractions
    curiosities = []
    for num in range(10,99):
        for denom in range(num+1,100):
            if is_curious_fraction(num,denom):
                curiosities.append((num,denom))

    #determine product of fractions
    numerator, denominator = int(1), int(1)
    for curiosity in curiosities:
        numerator *= curiosity[0]
        denominator *= curiosity[1]

    #reduce
    GCD = math.gcd(denominator,numerator)

    #result
    print(int(denominator/GCD))
    print('Runtime: {0}'.format(time.time()-stime))

