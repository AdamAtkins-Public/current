import os
import string
import time

"""
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key.
The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes.
The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (right click and 'Save Link/Target As...'),
a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words,
decrypt the message and find the sum of the ASCII values in the original text.
"""


def generate_key():
    key = ''
    for a in string.ascii_lowercase:
       key += a 
       for b in string.ascii_lowercase:
           key += b
           for c in string.ascii_lowercase:
               key += c
               yield key
               key = key[:-1]
           key = key[:-1]
       key = key[:-1]

key_conv = dict(zip(string.ascii_lowercase,range(97,123)))
def ascii_to_int(string):
    value = int(0)
    for i in range(len(string)):
        value = (value<<8)|key_conv[string[i]]
    return value

def decode_segment(ascii_values,segment,key):
    text = ''
    encoded = int(0)
    for e in range(len(segment)):#list of encoded characters
        encoded = (encoded<<8)|segment[e]
    decoded = encoded ^ key
    char = int(0)
    for d in range(len(segment)):
        char = (decoded>>(8*(len(segment)-1-d)))&255
        if char in ascii_values:
            text += ascii_values[char]
        else:
            text += '*'
    return text

def possible_key(text,word_list):
    for word in word_list:
        if text.find(word) > 0:
            return True
    return False

def sum_text_ascii(cipher,key):
    total = int(0)
    key_chain = []
    for i in range(3):
        key_chain.append((key>>8*(2-i))&255)
    for c in range(0,len(cipher)):
        total += cipher[c] ^ (key_chain[c%3])
    return total

if __name__ == '__main__':

    stime = time.time()

    ascii_values = dict(zip(range(97,123),string.ascii_lowercase))
    value = 65
    for c in string.ascii_uppercase:
        ascii_values[value] = c
        value += 1

    keys = generate_key()
    cipher = []
    with open("Project_Euler\python\data\p059_cipher.txt") as data:
        while True:
            line = data.readline()
            if line == '':
                break
            for entry in line.split(','):
                cipher.append(int(entry))

    word_list = ['Euler']
    solution_key = None
    while True:
        try:
            key = ascii_to_int(keys.__next__())
        except StopIteration:
            print('Update wordlist')
            break

        text = ''

        for seg in range(0,len(cipher),3):
            text += decode_segment(ascii_values,cipher[seg:seg+3],key)

        if possible_key(text,word_list):
            break

    print("Solution:{} Runtime:{}".format(sum_text_ascii(cipher,key),time.time()-stime))
