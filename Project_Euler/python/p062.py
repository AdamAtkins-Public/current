import os
import time

"""
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3).
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

def classify(n):
    classification = ''
    n_str = n.__str__()
    for i in range(10):
        classification += n_str.count(i.__str__()).__str__() + '*'
    return classification

if __name__ == '__main__':

    stime = time.time()

    cubes = dict()
    n = 0
    while True:
        n += 1
        class_n = classify(n**3)
        if class_n in cubes:
            cubes[class_n].append(n)
            if len(cubes[class_n]) == 5:#solution smallest member class n
                break
        else:
            cubes[class_n] = [n]
    print("Solution:{} Runtime:{}".format(sorted(cubes[class_n])[0]**3,time.time()-stime))
