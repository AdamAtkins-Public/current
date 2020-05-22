
import os
import time

'''
In the United Kingdom the currency is made up of pound (&) and pence (p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, &1 (100p), and &2 (200p).

It is possible to make 2 in the following way:

    1x(&)1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can &2 be made using any number of coins?
'''

#enumerate valid sets
def p031():
    #currency dictionary
    currency = { '2':200, '1':100, '50p':50, \
                 '20p':20, '10p':10, '5p':5, \
                 '2p':2, '1p':1}
    print(list(currency))

if __name__ == '__main__':
    stime = time.time()
    p031()
    print('Runtime:',time.time()-stime)

