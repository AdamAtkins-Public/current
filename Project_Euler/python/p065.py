import os
import time

"""
[...]https://projecteuler.net/problem=65[...]

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
"""
def func_():

    def iterative_(t,n,d):
        return (t*d)+n,d

    #generate 100 cf terms of e
    e_terms = [2,1,2]
    k = 2
    for i in range(1,98):
        if i%3 == 0:
            e_terms.append(2*k)
            k+=1
        else:
            e_terms.append(1)
    n = e_terms[-1]
    d = 1
    for term in range(len(e_terms)-1,0,-1):
        n,d = iterative_(e_terms[term-1],d,n)

    return n.__str__()

if __name__ == '__main__':
    stime = time.time()
    print("Solution:{} Runtime:{}".format(sum(int(d) for d in func_()),time.time()-stime))
