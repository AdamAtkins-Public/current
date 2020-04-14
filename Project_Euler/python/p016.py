
import os
import math
'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''


if __name__ == '__main__':
    n = (int(math.pow(2,1000))).__str__()
    sum = int(0)
    for i in range(len(n)):
        sum += int(n[i])
    print(sum)
