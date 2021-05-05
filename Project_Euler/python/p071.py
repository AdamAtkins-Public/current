import os
import math
import time

"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
"""

class ratio():

    def __init__(self,numerator,denominator):
        self.n = numerator
        self.d = denominator

    def __eq__(self, rat):
        return self.n == rat.num() and self.d == rat.denom()

    def __lt__(self,rat):
        return self.n*rat.denom()<self.d*rat.num()

    def __repr__(self):
        self.reduce()
        return "{}/{}".format(self.n,self.d)

    def __add__(self,rat):
        if self.n == 0:
            self.n = rat.num()
            self.d = rat.denom()
        else:
            denom = self.d * rat.denom()
            num = (rat.denom() * self.n) + (rat.num() * self.d)
            self.n = num
            self.d = denom
        self.reduce()

    def multiply(self,rat):
        self.n *= rat.num()
        self.d *= rat.denom()
        self.reduce()

    def num(self):
        return self.n
    def denom(self):
        return self.d

    def set_num(self,n):
        self.n = n

    def reduce(self):
        gcd = math.gcd(self.n,self.d)
        if not gcd == 0:
            self.n //= gcd
            self.d //= gcd
            if not gcd == 1:
                self.reduce()

if __name__ == '__main__':

    stime = time.time()

    max = ratio(3,7)
    min = ratio(2,5)
    next_ratio = None

    denom = 10**6
    while denom > 7:
        next_ratio = ratio((3*denom)//7,denom)
        while next_ratio < max:
            if next_ratio > min:
                min = ratio(next_ratio.num(),next_ratio.denom())
            next_ratio.set_num(next_ratio.num()+1)
        if denom < min.num():
            break
        denom -= 1

    print("Solution:{} Runtime:{}".format(min.num(),time.time()-stime))

