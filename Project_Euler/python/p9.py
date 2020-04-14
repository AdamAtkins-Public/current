
import os
import math

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def is_perfect_square(n):
    return math.sqrt(n) == int(math.sqrt(n))

if __name__ == '__main__':

    #Bruteforce
    a = int(3)
    b = int(0)
    c = int(0)
    found = False
    while True:
        b = a + 1
        while a + b + c < 1001:
            b = b + 1
            c = math.sqrt(math.pow(a,2) + math.pow(b,2))
            if a + b + c == 1000:
                found = True
                break
        if found:    
            break
        a = a + 1

    #Problem solution
    print(a*b*int(c))

