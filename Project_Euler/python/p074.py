import os
import time

"""
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169;
it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms,
but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""

def factorials(n):
    facts = {0:1, 1:1}
    for i in range(2,n+1):
        facts[i] = i * facts[i-1]
    return facts

def sum_factorials(facts,n):
    return sum(facts[int(d)] for d in n.__str__())


if __name__ == '__main__':
    
    stime = time.time()

    facts = factorials(9)
    chains = dict()
    count = int(0)
    for n in range(1,10**6):
        chain = [n]
        next = n
        while True:
            next = sum_factorials(facts,next)
            if next in chains:
                chains[n] = chains[next] + len(chain)
                if chains[n] == 60:
                    count += 1
                break
            if next in chain:
                index = chain.index(next)
                if index != 0:
                    chains[next] = len(chain)-index
                chains[n] = len(chain)
                if chains[n] == 60:
                    count += 1
                break
            chain.append(next)
    print("Solution:{} Runtime:{}".format(count,time.time()-stime))
