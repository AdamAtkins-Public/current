
import os
from pe_common import runtime_calculator

"""
A common security method used for online banking is to ask the user for three random characters from a passcode.
For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""

@runtime_calculator
def p079():

    logs = []
    with open('Project_Euler\python\data\p079_keylog.txt') as data:
        while True:
            line = data.readline()
            if line == '':
                break
            logs.append(line[:-1])
    
    digits = {digit.__str__():(set(),set()) for digit in range(10)}

    for entry in logs:
        #add tail values to post of digit 1
        for index in range(1,3):
            digits[entry[0]][1].add(entry[index])

        #add head values to pre of digit 2
        for index in range(0,1):
            digits[entry[1]][0].add(entry[index])

        #add tail values to post of digit 2
        for index in range(2,3):
            digits[entry[1]][1].add(entry[index])

        #add head values to pre of digit 3
        for index in range(0,2):
            digits[entry[2]][0].add(entry[index])

    #sort dict into value,key pairs; value is tuple (prior,post)
    pairs = [(value,key) for (key,value) in digits.items()]
    pairs = sorted(pairs,key=lambda x:len(x[0][0]))

    #by inspection, we see that the minimum passcode can be deduced from sequencial occurrence
    # digits are not repeated
    minimum_passcode = str()
    for pair in range(len(pairs)):
        #a digit that does not occur in file
        if len(pairs[pair][0][0]) == 0 and len(pairs[pair][0][1]) == 0:
            continue
        minimum_passcode += pairs[pair][1]

    return minimum_passcode

if __name__ == '__main__':
    p079()
