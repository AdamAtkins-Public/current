
import os

'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)
'''

class tree:
    class node:
        def __init__(self, val):
            self.value = val
            self.left = None
            self.right = None
            self.max_sum = None 

        def max_sum_recursive(self):
            if self.max_sum is None:
                if self.left is not None:
                    self.left.max_sum_recursive()
                    self.right.max_sum_recursive()
                    if self.left.max_sum > self.right.max_sum:
                        self.max_sum = self.value + self.left.max_sum
                    else:
                        self.max_sum = self.value + self.right.max_sum
                else:
                    self.max_sum = self.value
            return self.max_sum



    def __init__(self):
        self.head = self.node(None)

    def set_value(self, in_node, val):
        in_node.value = val

    def insert_node(self, parent, in_node, child='R'):
        if child == 'R':
            parent.right = in_node
        else:
            parent.left = in_node

    #binary tree print; this will not represent the structure
    #this method is used for debugging only
    def print_tree(self, in_node):
        print(in_node.value)
        if in_node.left is not None:
            self.print_tree(in_node.left)
        if in_node.right is not None:
            self.print_tree(in_node.right)

    #recursively determine maximum sum possible
    def max_sum_tree(self):
        return self.head.max_sum_recursive()



if __name__ == '__main__':
    a_tree = tree()
    data =( '75',
            '95 64',
            '17 47 82',
            '18 35 87 10',
            '20 04 82 47 65',
            '19 01 23 75 03 34',
            '88 02 77 73 07 63 67',
            '99 65 04 28 06 16 70 92',
            '41 41 26 56 83 40 80 70 33',
            '41 48 72 33 47 32 37 16 94 29',
            '53 71 44 65 25 43 91 52 97 51 14',
            '70 11 33 28 77 73 17 78 39 68 17 57',
            '91 71 52 38 17 14 91 43 58 50 27 29 48',
            '63 66 04 68 89 53 67 30 73 16 69 87 40 31',
            '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23') 
    processed = list()
    for line in data:
        terms = line.split(' ')
        converted = list()
        for term in terms:
            converted.append(int(term))
        processed.append(converted)

    #nonbinary insert
    leaves = list()
    item = int(0)
    a_tree.set_value(a_tree.head,processed[0][0])
    leaves.append(a_tree.head)
    for level in range(len(processed)-1):
        item = 0
        new_leaves = list()
        for leaf in leaves:
            #left child
            if item == 0:
                a_tree.insert_node(leaf,a_tree.node(processed[level+1][item]),'L')
                new_leaves.append(leaf.left)
                item += 1
            else:
                a_tree.insert_node(leaf,new_leaves[-1],'L')
            #right child
            a_tree.insert_node(leaf,a_tree.node(processed[level+1][item]),'R')
            new_leaves.append(leaf.right)
            item += 1
        leaves.clear()
        leaves = new_leaves

    print(a_tree.max_sum_tree())
