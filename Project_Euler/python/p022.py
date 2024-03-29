﻿
import os

'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by 
its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
'''

value_map = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7,
             'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13,
             'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19,
             'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25,
             'Z':26}

#returns list of data loaded from 'path'
def load_data(path):
    data = list()
    with open(path) as data_file:
        raw_data = data_file.read().split(',')
        for entry in raw_data:
            data.append(str(entry.strip('"')))
    return data

def name_score(name):
    sum = int(0)
    for letter in name:
        sum += value_map[letter]
    return sum

if __name__ == '__main__':
    data_loc = '\Project_Euler\python\data\p022_names.txt'
    #load and sort
    data = sorted(load_data(os.getcwd()+data_loc))

    total = int(0)
    for entry in range(len(data)):
        total += (entry+1)*name_score(data[entry])
    print(total)