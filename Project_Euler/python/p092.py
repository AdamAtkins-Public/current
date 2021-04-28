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

def square_sum(squares,n):
    k = int(0)
    while(n):
        k += squares[n % 10]
        n = n // 10
    return k

def insert_chain(cache,chain):
    for n in chain:
        cache[n] = None

def resolve(squares,cache,n):
    n = square_sum(squares,n)
    if n in cache:
        return 0
    else:
        return 1

def resolve_chain(squares,cache,n):
    chain = [n]
    while True:
        if n in cache:
            insert_chain(cache,chain)
            break
        if n == 89:
            break
        else:
            n = square_sum(squares,n)
            chain.append(n)



if __name__ == '__main__':

    stime = time.time()

    cache = {1:None}
    squares = dict()

    for i in range(0,10):
        squares[i] = i*i

    for i in range(1,(7*(9**2))+1):
        resolve_chain(squares,cache,i)

    count = int(0)
    for n in range(1,10**7):
        count += resolve(squares,cache,n)
        
    print("Solution:{} Runtime:{}".format(count,time.time()-stime))
