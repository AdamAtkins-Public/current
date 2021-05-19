
import os
import time

"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'),
a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 2^99 altogether!
If you could check one trillion (10^12) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""

#return sum of max path; triangle 2-dimensional [level][node]
def func_(triangle):
    for level in range(len(triangle)-2,-1,-1):
        for node in range(len(triangle[level])):
            triangle[level][node] += max(triangle[level+1][node],triangle[level+1][node+1])
    return triangle[0][0]

if __name__ == '__main__':

    stime = time.time()

    triangle = []
    with open('Project_Euler\python\data\p067_triangle.txt') as data:
        while True:
            line = data.readline()
            if line == '':
                break

            #convert str to int
            convert = lambda x: int(x)
            line_copy = line.strip('\n').split(" ")
            for e in range(len(line_copy)): line_copy[e] = convert(line_copy[e])

            triangle.append(line_copy)
    
    print("Solution:{} Runtime:{}".format(func_(triangle),time.time()-stime))

