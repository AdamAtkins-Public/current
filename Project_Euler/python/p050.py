import os
import time

"""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
# To improve runtime, store prime sums to limit, iteratively reduce lists by removing min and max locating consectuve primes sum

def gather_primes(limit):
    primes = {2:1}
    for number in range(3,limit+1,2):
        is_prime = True
        mod_break = int(number**0.5)
        for prime in primes:
            if mod_break < prime:
                break
            if number % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes[number] = 1
    return primes

def consecutive_search(primes, limit):
    longest_sequence = 0
    largest_prime = 0
    list_primes = sorted(list(primes))
    for i in range(0,len(list_primes)):
        for j in range(i+1,len(list_primes)):
            prime_sum = sum(prime for prime in list_primes[i:j])
            if prime_sum > limit:
                break
            if prime_sum in primes:
                if j-i > longest_sequence:
                    longest_sequence = j-i
                    largest_prime = prime_sum
    return largest_prime


if __name__ == '__main__':
    stime = time.time()
    primes = gather_primes(1000000) 
    largest_prime = consecutive_search(primes, 1000000)
    print("Solution: {0}\nRuntime: {1}".format(largest_prime,time.time()-stime))
