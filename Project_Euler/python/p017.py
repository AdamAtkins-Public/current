
import os
import math

'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters
and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

number_map = { 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',
              7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven',
              12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',
              20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty',
              70:'seventy', 80:'eighty', 90:'ninety'}

def recursive_number(num):
    phrase = None
    mod = None
    div = None
    if num <= 15:
        phrase = number_map[num]
    elif num < 20:
        mod = num % 10
        if mod == 8:
            phrase = number_map[mod] + 'een'
        else:
            phrase = number_map[mod] + 'teen'
    elif num < 100:
        div = int(math.floor(num/10))*10
        mod = num % 10
        if mod == 0:
            phrase = number_map[div]
        else:
            phrase = number_map[div] + number_map[mod]
    elif num < 1000:
        div = int(math.floor(num/100))
        mod = num % 100
        if mod == 0:
            phrase = number_map[div] + 'hundred'
        else:
            phrase = number_map[div] + 'hundredand' + recursive_number(mod)
    else:
        phrase = 'onethousand'#:)
    return phrase

if __name__ == '__main__':
    sum = int(0)
    for i in range(1,1001):
        sum += len(recursive_number(i))
    print(sum)
