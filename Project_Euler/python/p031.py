
import os

"""
In the United Kingdom the currency is made up of pound (�) and pence (p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, �1 (100p), and �2 (200p).

It is possible to make �2 in the following way:

    1ף1 + 1�50p + 2�20p + 1�5p + 1�2p + 3�1p

How many different ways can �2 be made using any number of coins?
"""

currency_value = { '2':200, '1':100, '50p':50,
                   '20p':20, '10p':10, '5p':5,
                   '2p':2, '1p':1}

#solution uses recursion
def delver(remaining_value, available_coins):
    count = 0
    if remaining_value <= 200:
        if remaining_value == 0:
            return 1
        elif remaining_value < 0:
            return 0
        count += delver(remaining_value-currency_value[available_coins[0]],
                        available_coins)
        if len(available_coins) > 1:
            count += delver(remaining_value, available_coins[1:])
    return count


if __name__ == '__main__':
    print(delver(200,list(currency_value)))
