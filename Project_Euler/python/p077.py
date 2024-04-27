
import os
import numpy
from pe_common import runtime_calculator
from p051 import erato_sieve

"""
It is possible to write ten as the sum of primes in exactly five different ways:

	7 + 3
	5 + 5
	5 + 3 + 2
	3 + 3 + 2 + 2
	2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
"""

def prime_summations(initial_value, initial_prime, primes):

	query = initial_value
	summations = 0
	prime_index = initial_prime
	queue = list()

	while True:

		prime = primes[prime_index]
		remainder = query - prime

		if remainder == 0:
		   summations += 1

		if remainder < prime:

			prime_index -= 1
			if prime_index < 0:
				if len(queue)==0: break
				query, prime_index = queue.pop()
			else:
				queue.append((remainder,prime_index))
		else:
			if prime_index > 0:
				queue.append((query,prime_index-1))
			query = remainder

	return summations

@runtime_calculator
def p077():
	summation = 0
	#p077 summations limit
	p077_limit = 5000

	#number of primes
	upper_limit = 1000

	primes = list(erato_sieve(upper_limit))
	prime_index = 0

	for initial_value in range(11,upper_limit):
		while primes[prime_index] < initial_value:
			prime_index+=1
			if prime_index > len(primes):
				error("Insufficient number of primes")
		if prime_summations(initial_value,prime_index,primes) > p077_limit:
			return initial_value.__str__()

if __name__ == '__main__':
	p077()
