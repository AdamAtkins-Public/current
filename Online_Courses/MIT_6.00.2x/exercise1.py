import os
import time

def yieldAllCombos_g(items):
    '''
        Solution
    '''
    N = len(items)
    # Enumerate the 3**N possible combinations   
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            if (i // (3 ** j)) % 3 == 1:
                bag1.append(items[j])
            elif (i // (3 ** j)) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)

def yieldAllCombos(items):
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(4**N):
        bag1 = []
        bag2 = []
        valid = True
        for j in range(N):
            if (i >> 2*j) & 3 == 3:
                valid = False
                break
            if (i >> 2*j) % 2 == 1:
                bag1.append(items[j])
            if (i >> 2*j+1) % 2 == 1:
                bag2.append(items[j])
        if valid:
            yield (bag1, bag2)

if __name__ == '__main__':

    items = (1,2,3,4,5,6,7,8,
             9,10,11,12,13,14)

    stime1 = time.time()
    combos = yieldAllCombos(items)
    for i in range(3**len(items)):
        combos.__next__()
    print('S1 time: ', time.time() - stime1)

    stime2 = time.time()
    combos = yieldAllCombos_g(items)
    for i in range(3**len(items)):
        combos.__next__()
    print('S2 time: ', time.time() - stime2)
