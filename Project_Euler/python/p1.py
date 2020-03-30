
import os

'''

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''

div_3 = 0
div_5 = 0
div_3_t = 0
div_5_t = 0
div_3_5 = 0
div_3_5_t = 0

upper_limit = 1000

while div_3 < upper_limit:
    div_3_t = div_3_t + div_3
    div_3 = div_3 + 3

while div_5 < upper_limit:
    div_5_t = div_5_t + div_5
    div_5 = div_5 + 5 

while div_3_5 < upper_limit:
    div_3_5_t = div_3_5_t + div_3_5
    div_3_5 = div_3_5 + 3*5 

print(div_3_t + div_5_t - div_3_5_t)
