import os
import math
import time
import functools

'''
    function 'prime_factors' is incorrect

    function 'runtime_calculator' prints the results of wrapped function with a calculated runtime
'''

def runtime_calculator(function):
    @functools.wraps(function)
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = function(*args,**kwargs)
        end_time = time.time()
        print(f"Result:{result}\nRuntime:{end_time - start_time}")
        return result
    return wrapper

@runtime_calculator
def prime_factors(n):
    factors = {1:1}
    if n % 2 == 0:
        factors[2] = 1
    for factor in range(3,math.floor(math.sqrt(n))+1,2):
        if n % factor == 0:
            factors[factor] = 1
    factors[n] = 1
    fact_l = list(factors)
    composites = list()
    if len(fact_l) > 2:
        #n is not prime
        for index_a in range(1,len(fact_l)):
            if index_a not in composites:
                for index_b in range(index_a+1,len(fact_l)):
                    if index_b not in composites:
                        if fact_l[index_b] % fact_l[index_a] == 0:
                            composites.append(index_b)
                            remainder = fact_l[index_b] // (fact_l[index_a]**factors[fact_l[index_a]])
                            if remainder % fact_l[index_a] == 0:
                                factors[fact_l[index_a]] += 1
    #remove composite numbers
    for composite in composites:
        del factors[fact_l[composite]]

    return factors

def test_wrapper():
    prime_factors(6)

def test_prime_factors():
    print(prime_factors(25))
    print(prime_factors(20))
    print(prime_factors(154))
    #print(prime_factors(1989))
    #print(prime_factors(14175))
    #print(prime_factors(600851475143))
    #print(prime_factors(60085147514323941950914037510801238471857084560924856093459123489948325897234980759817239841))
    #print(prime_factors(60085147514323941950914037510801238471857084560924856093))

if __name__ == '__main__':
    test_wrapper()
