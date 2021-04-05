import os
import time

"""
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome.
A number that never forms a palindrome through the reverse and add process is called a Lychrel number.
Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise.
In addition you are given that for every number below ten-thousand, it will either
(i) become a palindrome in less than fifty iterations, or,
(ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome.
In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers
"""

def is_palindromic(value):
    copy = value.__str__()
    for i in range(int((len(copy)/2))+1):
        if copy[i] != copy[-(i+1)]:
            return False
    return True

def reverse(value):
    copy = value.__str__()
    reverse = ""
    for i in range(len(copy),0,-1):
        reverse += copy[i-1]
    return reverse

if __name__ == '__main__':
    stime = time.time()
    count = int(0)
    sum = int(0)
    for i in range(0,10000):
        sum = i
        for k in range(50):
            sum += int(reverse(sum))
            if is_palindromic(sum):
                count +=1
                break
    print("Solution:{} Runtime:{}".format(10000-count, time.time()-stime))
