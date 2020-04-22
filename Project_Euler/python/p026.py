
import os
import time

'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

'''

#Forms a string representation of numerator/denominator parameters
#   'sub_seq' contains the start/end index of a cycle if one exists
def decimal_str(n,d):

    memo = {}
    dec_str = ''
    sub_seq = ()

    dec_str += str(n // d)
    dec_str += '.'
    remainder = n % d
    index = len(dec_str)-1 
    while remainder != 0:
        numerator = 10 * remainder
        value = numerator // d
        remainder = numerator % d
        index += 1
        if numerator in memo:
            #encountered a cycle
            sub_seq = (memo.get(numerator), index)
            break
        else:
            memo[numerator] = index
        dec_str += str(value)

    return dec_str, sub_seq

if __name__ == '__main__':

    stime = time.time()

    max_d = 1
    max_cycle = 0
    cycle_length = 0
    for d in range(2,1000):
        dec_str, cycle = decimal_str(1,d)
        if len(cycle) > 0:
            cycle_length = cycle[1] - cycle[0]
        if cycle_length > max_cycle:
            max_cycle = cycle_length
            max_d = d
    print(max_d)
    print('Runtime:',time.time()-stime)
