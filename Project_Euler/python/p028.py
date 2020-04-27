
import os 
import time

'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

def collect_diagonals(max_side):
    down_right, down_left, up_left, up_right = list(), list(), list(), list()
    diagonals = down_right, down_left, up_left, up_right
    side = int(-1)
    count = int(1)
    while side < max_side:
        side += 2
        for diagonal in diagonals:
            count += side-1
            diagonal.append(count)
    return diagonals


if __name__ == '__main__':
    stime = time.time()
    diagonals = collect_diagonals(1001)
    total = 0
    for diagonal in diagonals:
        total += sum(diagonal,0)
    #center counted 4 times
    print(total - 3)
    print('Runtime:', time.time()-stime)