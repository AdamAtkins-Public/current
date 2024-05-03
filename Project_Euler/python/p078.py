
import os
from pe_common import runtime_calculator

"""
Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

    OOOOO
    OOOO   O
    OOO   OO
    OOO   O   O
    OO   OO   O
    OO   O   O   O
    O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.
"""

# referencing:
# https://projecteuclid.org/journals/rocky-mountain-journal-of-mathematics/volume-34/issue-2/Recurrences-for-the-Partition-Function-and-Its-Relatives/10.1216/rmjm/1181069871.full


@runtime_calculator
def p078():

    # p078 limit
    def check_satisfiability_condition(pn):
        divisor = pow(10,6)
        return False if pn < divisor else pn % divisor == 0

    # Memoization of p(n)
    memo = {0:1,1:1,2:2}

    #initial value of n
    n = 3
    sumA = 0
    sumB = 0

    #Euler's pentagonal number reccurrence
    while True:
        partA = 0
        for k in range(1,n+1):
            partA = n - k*(3*k - 1)//2
            if partA < 0:
                break
            sumA += pow(-1,k-1)*memo[partA]
        partB = 0
        for k in range(1,n+1):
            partB = n - k*(3*k + 1)//2
            if partB < 0:
                break
            sumB += pow(-1,k-1)*memo[partB]

        memo[n] = sumA + sumB

        if check_satisfiability_condition(memo[n]):break

        sumA = 0
        sumB = 0
        n += 1
    return n.__str__()

if __name__ == '__main__':
    p078()
