
import os
import math
import time

"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the
concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital,
918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer
with (1,2, ... , n) where n > 1?
"""

def is_1to9_pandigital(string):
    digits = {}
    for i in range(len(string)):
        if int(string[i]) in digits: return False
        digits[int(string[i])] = 1
    for i in range(1,10):
        if i not in digits: return False
    return True

#Returns max pandigital for number n if one exists
# else returns 0
def p038(n):
    current_value = str()
    product = int(1)
    for product in range(1,10):
        current_value += str(n * product)
        if len(current_value) == 9:
            if is_1to9_pandigital(current_value):
               return int(current_value)
        if len(current_value) > 10:
                return 0
    return 0

if __name__ == '__main__':
    
    stime = time.time()

    max = 9999
    max_pandigital = int(0)
    current_value = int(0)
    for i in range(1,max+1):
        current_value = p038(i)
        if current_value > max_pandigital:
            max_pandigital = current_value

    print('Max 1 to 9 pandigital {0}\nRuntime: {1}'.format(max_pandigital, time.time()-stime))



