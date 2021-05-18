import os
import time

"""
All square roots are periodic when written as continued fractions [and can be written in the form: ...]

[projecteuler.net/problem=64]

[...]
How many continued fractions for N =< 10000 have an odd period?
"""

def func_(N):

    def iterative(N,base,num,c):
        d = N - c**2
        n = num * (base + abs(c))
        a = n//d
        r = n%d
        c = (r - num*base)//num
        return c,d//num,a

    base = int(N**0.5)
    cycle = dict()
    c = -1*base
    d = 1
    while True:
        c,d,a = iterative(N,base,d,c)
        hash = hash_(c,d,a)
        if hash in cycle: return len(cycle)
        else: cycle[hash] = True

def hash_(c,d,a):
    return "{}*{}*{}".format(c,d,a)

if __name__ == '__main__':

    stime = time.time()

    count = int(0)
    for i in range(2,10001):
        if i**0.5 != int(i**0.5):
            if func_(i) & 1 == 1:
                count +=1

    print("Solution:{} Runtime:{}".format(count,time.time()-stime))
