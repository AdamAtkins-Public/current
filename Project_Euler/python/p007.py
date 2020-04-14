
import os

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

if __name__ == '__main__':
#Bruteforce
    max = 10001
    i = int(3)
    primes = list()
    primes.append(2)
    count = int(1)
    while count < max:
        composite = False
        for k in range(len(primes)):
            if i % primes[k] == 0:#if i is composite
                composite = True
                break
        if not composite:
            primes.append(i)
            count = count + 1
        i = i + 2
    print(primes[-1])

