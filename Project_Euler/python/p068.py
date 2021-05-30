import os
import time

"""
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.

Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example),
each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.
Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings.
What is the maximum 16-digit string for a "magic" 5-gon ring?
"""

def chains():

    def copy(values):
        return set(values)

    def next_chain(chains,chain,values,b,V):
        if len(values) == 1:
            for v in values:
                if v + b + chain[0][1] == V:
                    chain.append((v,b,chain[0][1]))
                    chains.append(chain.copy())
                    chain.pop(-1)
        else:
            for a_ in list(values):
                values.remove(a_)
                for b_ in list(values):
                    if a_ + b_ + b == V:
                        values.remove(b_)
                        chain.append((a_,b,b_))
                        next_chain(chains,chain,copy(values),b_,V)
                        chain.pop(-1)
                        values.add(b_)
                values.add(a_)

    chains = []
    values = set(range(1,10))
    for a in list(values):
        values.remove(a)
        for b in list(values):
            values.remove(b)
            chain = [(10,a,b)]
            next_chain(chains,chain,copy(values),b,10+a+b)
            values.add(b)
        values.add(a)
    return chains

def max_arrange(chain):
    min_v = 11
    min_link = None
    outside_value = lambda x: x[0]
    index = int(0)
    for link in chain:
        if outside_value(link) < min_v:
            min_v = outside_value(link)
            min_link = index
        index += 1
    max_arrange = chain[min_link:]
    max_arrange.extend(chain[:min_link])
    return max_arrange

def concatenate(chain):
    result = ''
    for seg in chain:
        for link in seg:
            result += str(link)
    return result


if __name__ == '__main__':
    max = int(0)
    stime = time.time()
    for chain in chains():
        chain_v = int(concatenate(max_arrange(chain)))
        if max < chain_v:
            max = chain_v
    print("Solution:{} Runtime:{}".format(max,time.time()-stime))

