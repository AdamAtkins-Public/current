import os
import time

values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
char_values = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
subtractive_pairs = {'M':'C', 'D':'C', 'C':'X', 'L':'X', 'X':'I', 'V':'I', 'I':None}

def parse_(numeral):
    length = len(numeral)
    total = int(0)
    for i in range(length):
        if not i+1 == length:
            if is_subtractive(numeral,i):
                total -= 2*values[numeral[i]]
        total += values[numeral[i]]
    return total

def is_subtractive(numeral,i):
    q,p = numeral[i],numeral[i+1]
    return subtractive_pairs[p] == q

def form_minimum(value):
    string = ''
    denom = 1000
    while not denom == 1:
        string, value = form_segment(value,denom,string)
        denom //= 2
        string, value = form_segment(value,denom,string)
        denom //= 5
    string += 'I' * value
    return string

def form_segment(value,denom,string):
    remainder = value % denom
    frequency = value // denom
    string += frequency * char_values[denom]
    if remainder // (denom - values[subtractive_pairs[char_values[denom]]]) == 1:
        remainder -= denom - values[subtractive_pairs[char_values[denom]]]
        string += subtractive_pairs[char_values[denom]] + char_values[denom]
    return string, remainder

if __name__ == '__main__':

    stime = time.time()

    count = int(0)
    with open('Project_Euler\python\data\p089_roman.txt') as datafile:
        while True:
            line = datafile.readline()
            if line == '':
                break
            line = line[:-1]#scrub '\n'
            count += len(line) - len(form_minimum(parse_(line)))
    print('Solution:{} Runtime:{}'.format(count,time.time()-stime))
