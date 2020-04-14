
import os
import math
import time

'''
A palindromic number reads the same both ways.

The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

#BruteForce approach
def is_palindrome(n_string):
    length = len(n_string)
    i = 0
    j = length-1
    result = True
    while i < math.ceil(length/2):
        if n_string[i] != n_string[j]:
            result = False
            break
        i = i+1
        j = j-1
    return result

if __name__ == '__main__':

    stime = time.time()

#upperdiagonal of products
#distance from [0][0] = 0 [0][1] = 1 [0][2] = 2 [1][1] = 2
    left = 999
    right = 999
    distance = int(0)
    found = False
    while True:
        i = math.ceil(distance/2)
        k = math.floor(distance/2)
        while i >= 0:
            product = (left-i)*(right-k)
            if is_palindrome(str(product)):
                print(product)
                found = True
                break
            i = i - 1
            k = k + 1
        if found:
            break
        distance = distance + 1

    print('Runtime:', time.time() - stime)

