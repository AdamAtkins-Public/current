import os
import time

"""
The proper divisors of a number are all the divisors excluding the number itself.
For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers.
For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
"""

#brute
def divisors(n):
    div = [1]
    for i in range(2,int(n/2)+1):
        if n % i == 0:
            div.append(i)
    return div

def divisor_prop(max):
    dic = {1:1}
    for i in range(2,int(max/2)+1):
        if not i in dic:
            dic[i] = 1
        j=2
        while j*i < max:
            if not j*i in dic:
                dic[j*i] = 1 + i
            else:
                dic[j*i] += i
            j+=1
    for i in range(2,max):
        if not i in dic:
            dic[i] = 1

    return dic

def delver(start,dict):
    def delve(start,chain,dict):
        if chain[-1] > 1000000:
            return []
        if not chain[-1] in dict:
            dict[chain[-1]] = sum(div for div in divisors(chain[-1]))
        if dict[chain[-1]] == start:
            return chain.copy()
        elif dict[chain[-1]] in chain:
            return []
        else:
            chain.append(dict[chain[-1]])
            return delve(start,chain,dict).copy()

    chain = []
    chain.append(start)
    chain = delve(start,chain,dict)
    return chain

def memoize(values,memo):
    for value in values:
        memo[value] = False

if __name__ == '__main__':

    stime = time.time()

    max = 1000000
    dic = divisor_prop(max) 
    memo = dict()
    max_chain = []
    for i in range(1,max):
        chain = [i]
        if i in memo:
            continue
        while True:
            if chain[-1] > max or chain[-1] in memo:
                chain = []
                break
            if not chain[-1] in dic:
                dic[chain[-1]] = sum(div for div in divisors(chain[-1]))
            new_entry = dic[chain[-1]]
            if new_entry == chain[0]:
                memoize(chain,memo)
                break
            if new_entry in chain:
                memoize(chain[:chain.index(new_entry)],memo)
                chain = []
                break
            chain.append(new_entry)

        if len(chain) > len(max_chain):
            max_chain = chain.copy()

    print("Solution:{} Runtime:{}".format(sorted(list(max_chain))[0], time.time()-stime))
