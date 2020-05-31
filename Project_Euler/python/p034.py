
import os
import itertools

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

def factorial(n):
    factorials = {0:1, 1:1}
    for i in range(2,n+1): factorials[i] = factorials.get(i-1)*i
    return factorials

def string_to_int(string):
    int_str = ''
    for char in string: int_str += str(char)
    return int(int_str)

def bell_triangle(n):
   row, prev_row = list(), list()
   #B_0 = 1
   row.append(1)
   for k in range(1,n):
       prev_row = row.copy()
       row.clear()
       row.append(prev_row[-1])
       for i in range(len(prev_row)):
           row.append(prev_row[i] + row[i])
   return row[-1]

def sum_factorials(int_list, factorials):
    sum = int(0)
    for i in int_list: sum += factorials.get(int(i))
    return sum

def partitions(set):
    for k in range(len(set)):
        for l in range(len(set),k,-1):
            partition = set[k:l]
            yield partition

def hash_partition(partition):
    hash = ''
    for part in partition: hash += str(part)
    return int(hash)

if __name__ == '__main__':

    factorials = factorial(9)
    curious_numbers = []
    max_range = 1000000
    for i in range(10,max_range):
        int_list = []
        for char in str(i): int_list.append(int(char))
        if sum_factorials(int_list,factorials) == i:
            curious_numbers.append(i)
    print(sum(number for number in curious_numbers))

    #max_range = 15
    #permutation_set = []
    #sums = {}
    #curious_numbers = {} 
    #factorials = factorial(max_range)
    #for i in range(1,max_range+1): permutation_set.append(i)
    #permutations = itertools.permutations(permutation_set)
    #while True:
    #    try: 
    #        permutation = permutations.__next__()
    #        parts = partitions(permutation)
    #        while True:
    #            try:
    #                partition = parts.__next__()
    #                if len(partition) > 1:
    #                    part_hashed = hash_partition(sorted(partition))
    #                    if part_hashed not in sums:
    #                        sums[part_hashed] = sum_factorials(partition, factorials)
    #                    part_str = string_to_int(partition)
    #                    if part_str not in curious_numbers:
    #                        if sums.get(part_hashed) == part_str:
    #                            curious_numbers[part_str] = True
    #                            print(string_to_int(partition))
    #                        else:
    #                            curious_numbers[part_str] = False

    #            except StopIteration: break
    #    except StopIteration: break

    #for depth in range(2,max_range):
    #    for i in range(1,depth+1): permutation_set.append(i)
    #    permutations = itertools.permutations(permutation_set)
    #    print(permutation_set)
    #    while True:
    #        try: 
    #            permutation = permutations.__next__()
    #            parts = partitions(permutation)
    #            while True:
    #                try: 
    #                    partition = parts.__next__()
    #                    if partition in curious_numbers:
    #                        pass
    #                    elif len(partition) > 1:
    #                        if sum_factorials(partition, factorials) == string_to_int(partition):
    #                            print(partition)
    #                            curious_numbers[partition] = True
    #                        else:
    #                            curious_numbers[partition] = False 
    #                except StopIteration: break
    #        except StopIteration: break
    #    print(len(list(curious_numbers)))
    #    print(permutation_set)
    #    permutation_set = []

    #numbers = []
    #for number in curious_numbers:
    #    if curious_numbers.get(number):
    #        numbers.append(number)
    #print(numbers)
    
    #print('Sum of curious numbers 1->{0}: {1}'.format(max_range,sum(number for number in numbers)))

        


