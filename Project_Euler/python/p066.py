import os
import time

def m_(a,b,k):
    k = k.__abs__()
    #solutions to k | a+bm
    term_0 = int(0)
    while not (a+(b*term_0)) % k == 0:
        term_0 += 1
    i = int(0)
    while True:
        yield k*i + term_0
        i += 1

def minimal_m(a,b,k,D):
    gen_m = m_(a,b,k)
    minimum = D**2
    minimum_m = None
    while True:
        m = gen_m.__next__()
        value = m**2 - D
        value = value.__abs__()
        if value < minimum:
            minimum = value
            minimum_m = m
        else:
            break
    return minimum_m

#chakravala cycle, Pell equation, Brahmagupta's identity : Bhaskara's lemma
def Brahmagupta_cycle(D):

    a = int(1)
    b = int(1)
    k = None
    min_k = None
    min_k_v = float('inf')
    while True:
        k = a**2 - D
        if k.__abs__() < min_k_v:
            min_k_v = k.__abs__()
            min_k = k
        else:
            a-=1
            break
        a += 1
    k = min_k
    while True:
        if k == 1:
            return (a,b,D)
        m = minimal_m(a,b,k,D)
        a_old = a
        a = (a*m + D*b)//k.__abs__()
        b = (a_old + b*m)//k.__abs__()
        k = (m**2 - D)//k


if __name__ == '__main__':

    stime = time.time()

    max_x = int(-1)
    for i in range(2,1001):
        if i**0.5 == int(i**0.5):
            continue
        x,y,D = Brahmagupta_cycle(i)
        if x > max_x:
            max_x = x
            max_D = D

    print("Solution:{} Runtime:{}".format(max_D,time.time()-stime))
