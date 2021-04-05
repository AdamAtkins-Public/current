import os
import time

"""
A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
"""

def sum_digits(value):
    copy = value.__str__()
    sum = int(0)
    for digit in copy:
        sum += int(digit)
    return sum

if __name__ == '__main__':
    stime = time.time()
    a = 99
    b = 100
    current_max = int(0)
    while(a > 1):
        b = 100
        new_number = int(a ** b)
        sum = sum_digits(new_number)
        if sum > current_max:
            current_max = sum
        if len(new_number.__str__())*9 < current_max:
            break
        while(b > 1):
            b += -1
            new_number = int(a ** b)
            sum = sum_digits(new_number)
            if sum > current_max:
                current_max = sum
            if len(new_number.__str__())*9 < current_max:
                break
        a += -1
    print("Solution:{} Runtime:{}".format(current_max,time.time()-stime))
