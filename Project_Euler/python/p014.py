﻿
import os

'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 

Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

#return count of terms for starting number n
def collatz_chain_length(n):
    term_count = int(1)
    while n != 1:
        if n & 1 == 0:
            n = int(n/2)
        else:
            n = int(3*n + 1)
        term_count = term_count + 1
    return term_count


if __name__ == '__main__':
    max = int(0)
    count = int(0)
    max_start = int(1)
    for n in range(1,1000000):
        count = collatz_chain_length(n)
        if count > max: 
            max = count
            max_start = n
    print(max_start)