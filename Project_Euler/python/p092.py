import os
import time

"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

def sum_square_digits(n,squares):
    return sum(squares[int(digit)] for digit in n.__str__())

def resolve_chain(values,n,squares):
    if n in values[1]:
        return 1
    elif n in values[0]:
        return 0
    else:
        chain = [n]
        while True:
            if n in values[1]:
                enter_chain(values[1],chain)
                return 1
            if n in values[0]:
                enter_chain(values[0],chain)
                return 0
            n = sum_square_digits(n,squares)
            if n in chain:
                if n == 1:
                    enter_chain(values[0],chain)
                    return 0
                if n == 89:
                    for value in chain:
                        enter_chain(values[1],chain)
                    return 1
            chain.append(n)

def enter_chain(value,chain):
    for n in chain:
        value[n] = 1

if __name__ == '__main__':

    stime = time.time()

    squares = dict()
    for i in range(10):
        squares[i] = i**2

    values = [dict(),dict()]
    count = int(0)

    for n in range(1,10**7):
        count += resolve_chain(values,n,squares)
        
    print("Solution:{} Runtime:{}".format(count,time.time()-stime))
