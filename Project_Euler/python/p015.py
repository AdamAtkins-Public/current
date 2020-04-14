
import os

'''
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
'''

def iterative_count(max):
    matrix = list()
    for i in range(max+1):
        matrix.append(list())
        for j in range(max+1):
            matrix[i].append(int(1))
    for i in range(1,max+1):
        for j in range(1,max+1):
            if i == j:
                matrix[i][j] = matrix[i][j-1] * 2
                break
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    return matrix[max][max]

#Alternatively consider 40 choose 20, Pascals triangle, binomial theorem. 
if __name__ == '__main__':
    print(iterative_count(20))
    pass