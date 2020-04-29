
import os
import time

'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

def p030(n_max):

    def list_digits(n):
        digits = list()
        n_string = str(n)
        for digit in range(len(n_string)):
            digits.append(int(n_string[digit]))
        return digits

    #collect values where condition is true
    values = list()
    for n in range(2,n_max):
        digits = list_digits(n)
        sum = int(0)
        for digit in digits:
            sum += int(digit ** 5)
        if sum == n:
            values.append(n)
    return values

#find upper limit
def def_limit(exp):
    n = int(1)
    while((n*(9**exp)) > 10**n):
        n += 1
    return n*(9**exp)


if __name__ == '__main__':
    stime = time.time()
    print(sum(p030(def_limit(5))))
    print('Runtime:', time.time()-stime)
