import os
import time

"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below).
But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below);
if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:
Hand	 	Player 1	 	            Player 2	 	                    Winner
1	 	5H 5C 6S 7S KD Pair of Fives 	2C 3S 8S 8D TD Pair of Eights 	 	Player 2
2	 	5D 8C 9S JS AC Highest card Ace 2C 5C 7D 8S QH Highest card Queen 	Player 1
3	 	2D 9C AS AH AC Three Aces	 	3D 6D 7D TD QD Flush with Diamonds 	Player 2
4	 	4D 6S 9H QH QC Pair of Queens   Highest card Nine 	3D 6D 7H QD QS Pair of Queens Highest card Seven Player 1
5	 	2H 2D 4C 4D 4S Full House With Three Fours  	3C 3D 3S 9S 9D Full House with Three Threes 	Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): 
the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

facevalue = { '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
              '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14 }

def eval_facecard(card):
    return facevalue[card[0]]

def return_hand_value(hand):
    value = 0
    flush = True
    straight = True
    highcard = ''
    suit = hand[0][1]
    for card in range(len(hand)-1):
        if flush:
            if hand[card+1][1] != suit:
                flush = False
        if straight:
            if eval_facecard(hand[card+1]) != eval_facecard(hand[card])+1:
                straight = False
        if value == 0:#highcard
            if hand[card][0] == hand[card+1][0]:
                value = 2
                highcard = hand[card+1]
            continue
        if value == 2:#pair
            if hand[card+1][0] == highcard[0]:
                value = 8
                highcard = hand[card+1]
            elif hand[card][0] == hand[card+1][0]:
                value = 4
                highcard = hand[card+1]
            continue
        if value == 4:#twopair
            if hand[card+1][0] == highcard[0]:
                value = 64#fullhouse
                highcard = hand[card+1]
            continue
        if value == 8:#3ofakind
            if hand[card+1][0] == highcard[0]:
                value = 128#4ofakind
                highcard = hand[card+1]
            elif hand[card][0] == hand[card+1][0]:
                value = 64
                highcard = hand[card+1]
            continue
    if straight and flush:
        if hand[-1][1] == 'A':
            value = 512
            highcard = hand[-1]
        else:
            value = 256
            highcard = hand[-1]
    if value < 64:
        if flush:
            value = 32
            highcard = hand[-1]
        elif straight:
            value = 16
            highcard = hand[-1]
    if value == 0:
        highcard = hand[-1]
    return value, highcard

if __name__ == '__main__':

    stime = time.time()
    count = int(0)
    with open("Project_Euler\python\data\p054_poker.txt") as data_file:
        for line in data_file:
            hands = line.split(' ')
            hands[-1] = hands[-1][:2]#scrub newline
            hand1 = sorted(hands[:5],key=eval_facecard)
            hand2 = sorted(hands[5:],key=eval_facecard)

            value1, hc1 = return_hand_value(hand1)
            value2, hc2 = return_hand_value(hand2)
            if value1 == value2:
                if value1 == 4 or value2 == 4:
                    print('check')
                if eval_facecard(hc1) == eval_facecard(hc2):
                    for i in range(5):
                        if eval_facecard(hand1[4-i]) == eval_facecard(hand2[4-i]):
                            continue
                        elif eval_facecard(hand1[4-i]) > eval_facecard(hand2[4-i]):
                            count+=1
                            break 
                        else:
                            break
                elif eval_facecard(hc1) > eval_facecard(hc2):
                    count+=1
            elif value1 > value2:
                count+=1
    print("Solution:{} Runtime:{}".format(count,time.time()-stime))
