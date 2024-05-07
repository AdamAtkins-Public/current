
import os
import decimal 
from pe_common import runtime_calculator

"""
It is well known that if the square root of a natural number is not an integer, then it is irrational.
The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is

1.41421356237309504880

and the digital sum of the first one hundred decimal digits is

475

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""

def sum_decimal_digits(n):
    sum = 0
    root = decimal.Decimal(n).sqrt().__str__()
    for digit in range(101):
        if not root[digit] == '.':
            sum += int(root[digit])
    return sum

@runtime_calculator
def p080():
    numbers = []
    #sieve rational squares
    for number in range(101):
        numbers.append(1)
    for number in range(11):
        numbers[number*number] = 0

    decimal.getcontext().prec = 102
    sum = 0
    for number in range(len(numbers)):
        if numbers[number] == 1:
            sum += sum_decimal_digits(number)
    return sum

if __name__ == '__main__':
    p080()