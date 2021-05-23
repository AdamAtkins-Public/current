import os
import math
import time

"""
It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way,
but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found;
for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?
"""
#Euclid's Formula
def triple_(m,n):
    return (int(m**2 - n**2), int(2*m*n), int(m**2 + n**2))

def is_coprime(m,n):
    return 1 == math.gcd(m,n)

if __name__ == '__main__':

    stime = time.time()

    #Euclid's formula
    max_v = 1500000
    n = 1
    primatives = dict()
    count = int(0)
    while True:
        m = n + 1
        b = True
        tsum = sum(s for s in triple_(m,n))
        while tsum < max_v:
            b = False
            if is_coprime(m,n):
                if tsum in primatives:
                    primatives[tsum] += 1
                else:
                    primatives[tsum] = 1
            m+=2
            tsum = sum(s for s in triple_(m,n))
        n+=1
        if b: break
    for k in list(primatives):
        c = 2
        while c*k <= max_v:
            if not c*k in primatives:
                primatives[c*k] = primatives[k]
            else:
                primatives[c*k] += primatives[k]
            c+=1
    for i in range(1,1500001):
        v = i
        k = 1
        while True:
            if v in primatives:
                if primatives[v] == 1:
                    count += 1
                break
            else:
                k += 1
                v = i/k
                if v == int(i/k) and v > 1:
                    continue
                else:break
    print("Solution:{} Runtime:{}".format(count,time.time()-stime))
