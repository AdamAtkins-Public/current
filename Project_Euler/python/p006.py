
import os
import math

'''
The sum of the squares of the first ten natural numbers is,
1^2+2^2+...+10^2=385

The square of the sum of the first ten natural numbers is,
(1+2+...+10)^2=55^2=3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

#Gauss
def sum_from_1_to_n(n):
    return int((n*(n+1))/2)

#Square pyramidal number
def square_pyramidal_number(n):
    return int((n*(n+1)*(2*n+1))/6)

def pe_p6(n):
    return int(math.pow(sum_from_1_to_n(n),2) - square_pyramidal_number(n))

if __name__ == '__main__':
    n = 10
    print(pe_p6(n))

    n = 100
    print(pe_p6(n))
