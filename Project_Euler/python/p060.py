import os
import time

"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
def generate_key(old,value):
    return old + '*' + value.__str__()

def key_length(key):
    count = int(0)
    for digit in key:
        if digit == '*': count += 1
    return count

def is_prime(n):
    if n == 2:
        return True
    if n & 1 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

# Depth first, should not deplete stack resources
# could use dynamic programming optimization
def dictionary_delver(d,key,prime):

    new_prime_key = generate_key(key,prime)
    if key_length(new_prime_key) == 5:
        return new_prime_key

    if new_prime_key not in d:
        d[new_prime_key] = []

    solution = None
    values = d[key]
    for value in values:
        if is_prime(int(prime.__str__()+value.__str__())):
            if is_prime(int(value.__str__()+prime.__str__())):
                solution = dictionary_delver(d,generate_key(key,value),prime)
                if solution is not None:
                    break
    d[key].append(prime)
    return solution 

if __name__ == '__main__':
    stime = time.time()
    dictionary = {"":[]}
    n = 1
    while True:
        n += 2
        if is_prime(n):
            solution = dictionary_delver(dictionary,"",n)
            if solution is not None:
                break
    print("Solution:{} Runtime:{}".format(sum(int(value) for value in solution.split('*')[1:]), time.time()-stime))
