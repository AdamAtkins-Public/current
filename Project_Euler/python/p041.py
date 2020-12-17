import os
import math
import itertools
import time

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

def get_ndigit_permuter(n):
    n_digits = []
    for i in range(1,n+1):
        n_digits.append(str(i))
    n_digits.reverse()
    return itertools.permutations(n_digits)

def concatenate_ndigit_string(ndigit_str): 
    number = str()
    for digit in ndigit_str:
        number += digit
    return int(number)

def is_prime(n):
    if n == 2:
        return True
    elif n < 2:
        return False
    if n & 1 == 0:
        return False
    for i in range(3, math.ceil(math.sqrt(n)+1), 2):
        if n % i == 0:
            return False
    return True

#Start at 7 since n = 8 and n = 9 digitial root are divisible by 3
def largest_pandigital_prime():
    largest_prime = -1
    n = 7
    while(n > 2):
        permuter = get_ndigit_permuter(n)
        try:
            while(True):
                number_string = permuter.__next__()
                number = concatenate_ndigit_string(number_string)
                if number > largest_prime:
                    if is_prime(number):
                        largest_prime = number
        except StopIteration:
            if largest_prime > -1:
                break
            n = n - 1
    return largest_prime


if __name__ == '__main__':
    stime = time.time()
    prime = largest_pandigital_prime()
    print("Largest n-digit pandigital prime: {0}\nRuntime: {1}".format(prime,(time.time()-stime)))
