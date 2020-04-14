
import os
import p12 #list_factor(n)

'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''


def list_abundant(limit):
    abundant_numbers = list()
    for n in range(1,limit):
        if sum(p12.list_factors(n)[:-1]) > n:
            abundant_numbers.append(n)
    return abundant_numbers

if __name__ == '__main__':

    abundant_numbers = list_abundant(28124)
    abundant_sums = list()
    target_numbers = list()
    limit = 28124

    for a in range(len(abundant_numbers)):
        for b in range(a,len(abundant_numbers)):
            sum_ab = abundant_numbers[a] + abundant_numbers[b]
            if sum_ab > limit: 
                break
            abundant_sums.append(sum_ab)
    abundant_sums.sort()

    index = int(0)
    for n in range(1, limit):
        for a_sum in range(index, len(abundant_sums)):
            if n < abundant_sums[a_sum]:
                target_numbers.append(n)
                break
            if n == abundant_sums[a_sum]:
                break
            index += 1
    print(sum(target_numbers))
