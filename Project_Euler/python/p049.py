import os
import math
import time

"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

def is_prime(n):
    if n == 2:
        return True
    elif n < 2:
        return False
    if n & 1 == 0:
        return False
    for i in range(3, math.ceil(math.sqrt(n)+1), 2):
        if n % i == 0:
            return False
    return True

def get_groups():
    groups = dict()
    group_value = []
    for digit in range(10):
        group_value.append(1<<3*digit)

    for number in range(1000,10000):
        number_value = 0
        for digit in str(number):
            number_value += group_value[int(digit)]
        if number_value not in groups:
            groups[number_value] = [number]
        else:
            groups.get(number_value).append(number)
    return groups

def filter_groups():
    groups = get_groups()
    target_sequences = list()
    valid_sequences = list()
    valid_sequence = list()
    differences = dict()
    for group in list(groups):
        numbers = groups.get(group)
        valid_sequences.clear()
        #filter small groups
        if len(numbers) < 3:
            continue
        #filter even numbers from groups
        for number in list(numbers):
            if number & 1 == 0:
                numbers.remove(number)
        #filter small groups
        if len(numbers) < 3:
            continue
        #check increasing sequence |numbers|^2 ouch
        differences.clear()
        for i in range(len(numbers)-1):
            for j in range(i+1,len(numbers)):
                difference = numbers[j] - numbers[i]
                if difference not in differences:
                    differences[difference] = [(numbers[i],numbers[j])]
                else:
                    differences.get(difference).append((numbers[i],numbers[j]))
        for difference in differences:
            pairs = differences.get(difference)
            if len(pairs) < 2:
                continue
            for pair_i in range(len(pairs)-1):
                for pair_j in range(pair_i+1,len(pairs)):
                    if pairs[pair_i][1] == pairs[pair_j][0]:
                        valid_sequences.append([pairs[pair_i][0],pairs[pair_i][1],pairs[pair_j][1]])
        #check if sequence is prime
        for sequence in list(valid_sequences):
            for number in sequence:
                if not is_prime(number):
                    valid_sequences.remove(sequence)
                    break
        for sequence in valid_sequences:
            target_sequences.append(sequence)
    return target_sequences

if __name__ == '__main__':
    stime = time.time()
    target = str()
    target_sequences = filter_groups()
    for sequence in target_sequences:
        if sequence != list([1487,4817,8147]):
            target_sequence = sequence
    for number in target_sequence:
        target += str(number)
    print("Solution: {0}\nRuntime: {1}".format(target,time.time()-stime))
