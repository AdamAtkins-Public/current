
import os
import math

"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def is_palindrome(string):
    for i in range(math.ceil(len(string)/2)):
        if not string[i] == string[(len(string)-1)-i]:
            return False
    return True

if __name__ == '__main__':
    palindromic = []
    target = 1000000
    for i in range(target):
        if is_palindrome(str(i)) and is_palindrome(str(bin(i)[2:])):
            palindromic.append(i)
    print(sum(number for number in palindromic))
