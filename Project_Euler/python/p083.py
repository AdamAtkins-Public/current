import os
import time
import numpy as np

"""
NOTE: This problem is a significantly more challenging version of Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
by moving left, right, up, and down, is indicated in bold red and is equal to 2297.
Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down in matrix.txt
(right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""

class heap():

    def __init__(self,nparray):
        self.heap = nparray
        for i in range(len(self.heap)+1//2,-1,-1):
            self.heapify(i)

    def __len__(self):
        return len(self.heap)

    #recursively heapify from point in tree to root
    def update_key(self, index):
        l = self.left(index)
        r = self.right(index)
        if l <= len(self.heap)-1 and l > 0 and self.heap[l] < self.heap[index]: 
            smallest = l
        else: 
            smallest = index
        if r <= len(self.heap)-1 and r > 0 and self.heap[r] < self.heap[smallest]:
            smallest = r
        if not smallest == index:
            self.swap(index,smallest)
        if not self.parent(index) == -1:
            self.update_key(self.parent(index))

    #heapify from point to terminal condition
    def heapify(self,index):
        l = self.left(index)
        r = self.right(index)
        if l <= len(self.heap)-1 and self.heap[l] < self.heap[index]: 
            smallest = l
        else: 
            smallest = index
        if r <= len(self.heap)-1 and self.heap[r] < self.heap[smallest]:
            smallest = r
        if not smallest == index:
            self.swap(index,smallest)
            self.heapify(smallest)

    def pop(self):
        if len(self.heap) < 1:
            return None
        #return minimum_value
        minimum = self.heap[0]
        self.swap(0,len(self.heap)-1)
        self.heap = np.delete(self.heap,len(self.heap)-1)
        self.heapify(0)
        return minimum

    def index_of_linear(self,object):
        return np.argwhere(self.heap == object)[0][0]

    def parent(self,index):
        return ((index+1)//2)-1
    def left(self,index):
        return ((index+1)*2)-1
    def right(self,index):
        return (index+1)*2

    def swap(self,a,b):
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp

class vertex():

    def __init__(self, row, column, value):
        self.r = row
        self.c = column
        self.v = value
        self.d = float('inf')
        self.p = None

    def __str__(self):
        return "Row:"+str(self.r)+" Column:"+str(self.c)+" Value:"+str(self.v)+" Distance:"+str(self.d)

    def __lt__(self,v):
        return self.distance() < v.distance()

    def __le__(self,v):
        return self.distance() <= v.distance()

    def value(self):
        return self.v
    def row(self):
        return self.r
    def column(self):
        return self.c
    def distance(self):
        return self.d
    def predecessor(self):
        return self.p

    def set_distance(self,dist):
        self.d = dist
    def set_predecessor(self,pred):
        self.p = pred

def adjacency_list(v,matrix,row_max,col_max):
    adj = []
    if v.row() + 1 < row_max + 1:
        adj.append(matrix[v.row()+1][v.column()])#down
    if v.column() + 1 < col_max + 1:
        adj.append(matrix[v.row()][v.column()+1])#right
    if v.row() - 1 > -1:
        adj.append(matrix[v.row()-1][v.column()])#up
    if v.column() - 1 > -1:
        adj.append(matrix[v.row()][v.column()-1])#left
    return adj

def heap_relax(v,u):
    if u.distance() > v.distance() + u.value():
        u.set_distance(v.distance()+u.value())
        u.set_predecessor(v)
        return True
    return False 

if __name__ == '__main__':

    stime = time.time()

    pilot_vertex = vertex(0,0,1)
    v_array = np.array(pilot_vertex)
    v_array = np.delete(v_array,0)
    matrix = []
    row = int(-1)
    with open("Project_Euler\python\data\p083_matrix.txt") as data:
        while True:
            line = data.readline().split(',')
            if line[0] == '':
                break
            matrix.append([])
            row += 1
            column = int(0)
            for v in line:
                matrix[row].append(vertex(row,column,int(v)))
                v_array = np.append(v_array,matrix[row][column])
                column += 1

    row_max = row
    col_max = column-1

    #initial position
    min_distance = float('inf')

    matrix[0][0].set_distance(matrix[0][0].value())
    hq = heap(v_array)

    while not len(hq) == 0:
        v = hq.pop()
        for u in adjacency_list(v,matrix,row_max,col_max):
            if heap_relax(v,u):
                hq.update_key(hq.index_of_linear(u))

    print('Solution:{} Runtime:{}'.format(matrix[row_max][col_max].distance(),time.time()-stime))
