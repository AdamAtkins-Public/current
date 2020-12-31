
import os
import itertools

"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""
def get_ndigit_permuter(n):
    n_digits = []
    for i in range(0,n+1):
        n_digits.append(str(i))
    n_digits.reverse()
    return itertools.permutations(n_digits)

def concatenate_string(n_string):
    result = str()
    for n in n_string:
        result += n
    return result

def test_divisibility_property(n_string):
    prime_values = [2,3,5,7,11,13,17]
    con_n_string = concatenate_string(n_string)
    iteration = 9
    for prime in reversed(prime_values):
        if int(con_n_string[iteration-3:iteration]) % prime != 0:
            return False
        iteration -= 1
    return True



#Attempt to use dynamic programming to improve runtime
def get_ndigit_choose_r_permuter(n,r):
    n_digits = []
    for i in range(0, n+1):
        n_digits.append(str(i))
    return itertools.permutations(n_digits,r)

#keys are prime values, values are 3 digit strings such that key divides value
def divisibility_dictionary():

    nstring_permuter = get_ndigit_choose_r_permuter(9,3)
    prime_values = [2,3,5,7,11,13,17]

    #initialize dictionary
    divisibilty_dictionary = dict()
    for prime in prime_values: divisibilty_dictionary[prime] = []
    while(True):
        try:
            n_string = nstring_permuter.__next__()
            con_n_string = concatenate_string(n_string)
            for prime in prime_values:
                if int(con_n_string) % prime == 0:
                    divisibilty_dictionary.get(prime).append(con_n_string)
        except StopIteration:
            break
    return divisibilty_dictionary

#returns True if digit is found in numberlist
def digit_check(number,number_list):
    number_mod = number[0]
    for digit in number_mod:
        for n in number_list:
            if n.find(digit) != -1:
                return True
    return False


#Delver of tree search
def div_delver(div_dict,prime_numbers,prime_index,number_list,pandigitals):
    #Base case; we've found a pandigital
    if prime_index == -1:
        pandigital = number_list[0]
        for number in number_list[1:]: pandigital = number[0] + pandigital
        for i in range(0,10):
            if pandigital.find(str(i)) == -1:
                pandigital = str(i) + pandigital
        pandigitals[pandigital] = int(pandigital)
    else:
        for number in div_dict[prime_numbers[prime_index]]:
            #digit check
            if digit_check(number,number_list):
                continue
            #recursion
            elif number.endswith(number_list[-1][0:2]):
                number_list.append(number)
                div_delver(div_dict,prime_numbers,prime_index-1,number_list,pandigitals)
                number_list.remove(number)





if __name__ == '__main__':
    #Brute force
    #nstring_permuter = get_ndigit_permuter(9)
    #sum = 0
    #while(True):
    #    try:
    #        n_string = nstring_permuter.__next__()
    #        if test_divisibility_property(n_string):
    #            sum += int(concatenate_string(n_string))
    #    except StopIteration:
    #        break
    #print(sum)

    #Using dynamic programming
    number_list = []
    prime_values = [2,3,5,7,11,13,17]
    pandigitals = {}
    div_dict = divisibility_dictionary()
    #collect pandigitals
    for number in div_dict[17]:
        number_list.append(number)
        div_delver(div_dict,prime_values,5,number_list,pandigitals)
        number_list.clear()

    print(sum(value for value in pandigitals.values()))
