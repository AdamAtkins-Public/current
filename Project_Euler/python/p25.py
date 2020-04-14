
import os

'''
The Fibonacci sequence is defined by the recurrence relation:

    F_n = F_n−1 + F_n−2, where F_1 = 1 and F_2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''


def next_Fib_num(a,b):
    return a + b

def p25(target):
    Fib_a = 1
    Fib_b = 1
    Fib = int()
    Fib_index = int(2)
    while len(str(Fib)) < target:
        Fib = next_Fib_num(Fib_a, Fib_b)
        Fib_a = Fib_b
        Fib_b = Fib
        Fib_index += 1
    return Fib_index

if __name__ == '__main__':
    target = 1000 
    print(p25(target))