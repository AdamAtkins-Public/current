
import os

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier,
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

#determine if a string representation of a product is pandigital
def is_pandigital(int_string):
    values = {}
    if len(int_string) > 9:
        return False
    for char in int_string:
        if char not in values:
            values[char] = 1
        else:
            return False
    for i in range(len(int_string)):
        if str(i+1) not in values:
            return False
    return True

def concat_product(a, b):
    return str(a*b)+str(a)+str(b)

if __name__ == '__main__':
    ##Tests
    #print(is_pandigital('123'))
    #print(is_pandigital('4123'))
    #print(is_pandigital('41234'))
    #print(is_pandigital('41523'))
    #print(concat_product(2,4))
    #print(is_pandigital(concat_product(39,186)))

    #brute force solution
    a_max = 1000000
    b_max = 1000000
    products = []
    for a in range(1,a_max):
        for b in range(a, b_max):
            product = concat_product(a,b)
            if len(product) > 9:
                break
            if is_pandigital(product):
                if len(product) == 9:
                    products.append(a*b)
    print(sum(product for product in set(products)))
