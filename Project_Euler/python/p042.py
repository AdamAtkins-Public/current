
import os
import time
import string

"""
The nth term of the sequence of triangle numbers is given by, tn = (1/2)n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

def load_words(path):
    data = list()
    with open(path) as data_file:
        raw_data = data_file.read().split(',')
        for entry in raw_data:
            data.append(str(entry.strip('"')))
    return data

def triangle_number(n):
    return int((1/2)*n*(n+1))

def convert_word(word, values):
    value = 0
    for letter in word:
        value += int(values[letter])
    return int(value)

#values = {
#           'A':1, 'B':2, 'C':3, 'D':4, 'E':5,\
#           'F':6, 'G':7, 'H':8, 'I':9, 'J':10,\
#           'K':11, 'L':12, 'M':13, 'N':14, 'O':15,\
#           'P':16, 'Q':17, 'R':18, 'S':19, 'T':20,\
#           'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26
#         }

#Neat reduction from Project Euler thread
values = dict(zip(string.ascii_uppercase,range(1,27)))

if __name__ == '__main__':
    stime = time.time()
    path = '\Project_Euler\python\data\p042_words.txt'
    words = load_words(os.getcwd()+path)
    triangle_numbers = {-1:-1}
    max_triangle_number = -1
    word_count = 0
    for word in words:
        word_value = convert_word(word, values)
        while(word_value > max_triangle_number):
            next_triangle_number = triangle_number(len(triangle_numbers))
            triangle_numbers[len(triangle_numbers)] = next_triangle_number 
            max_triangle_number = next_triangle_number
        if word_value in triangle_numbers.values():
            word_count += 1
    print("Number of triangle words: {0}\nRuntime: {1}".format(word_count,time.time()-stime))


