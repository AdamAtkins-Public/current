
import os
import itertools
import time

if __name__ == '__main__':
    

    p_set = ('0', '1', '2', '3',
             '4', '5', '6', '7',
             '8', '9')

    target = 1000000 

    stime = time.time()
    p_t = itertools.permutations(p_set)
    for i in range(target-1):
        p_t.__next__()
    print(p_t.__next__())
    print(time.time() - stime)
