import os
import time
import random

"""
A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance in a clockwise direction.
Without any further rules we would expect to visit each square with equal probability: 2.5%.
However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail,
if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the top of the respective pile and,
after following the instructions, it is returned to the bottom of the pile.
There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement;
any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.

    Community Chest (2/16 cards):
        Advance to GO
        Go to JAIL
    Chance (10/16 cards):
        Advance to GO
        Go to JAIL
        Go to C1
        Go to E3
        Go to H2
        Go to R1
        Go to next R (railway company)
        Go to next R
        Go to next U (utility company)
        Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular square.
That is, the probability of finishing at that square after a roll.
For this reason it should be clear that, with the exception of G2J for which the probability of finishing on it is zero,
the CH squares will have the lowest probabilities, as 5/8 request a movement to another square,
and it is the final square that the player finishes at on each roll that we are interested in.
We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of jail",
assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to produce strings that correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00.
So these three most popular squares can be listed with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.
"""

#Naive simulation
_board = dict(zip(range(0,40),[0.0]*40))
_chance_deck = ["GO","JAIL","C1","E3","H2","R1","NR","NR","NU","GB3",
                "None","None","None","None","None","None"]
_communitychest_deck = ["GO","JAIL",
                        "None","None","None","None","None",
                        "None","None","None","None","None",
                        "None","None","None","None"]

def dice_roll(sides):
    return (random.randint(1, sides),random.randint(1, sides))

#railrroads at 5,15,25,35
def next_rr(square):
    if square > 35 and square < 5: return 5
    if square > 5 and square < 15: return 15
    if square > 15 and square < 25: return 25
    if square > 25 and square < 35: return 35
    return (square + 10) % 40

#utilities at 12 and 28
def next_util(square):
    if square > 28 or square < 12: return 12
    if square > 12 and square < 28: return 28

#converts chance cards to destination square
def convert_chance(square, card):
    if card == "GO": return 0
    elif card == "JAIL": return 10
    elif card == "C1": return 11
    elif card == "E3": return 24
    elif card == "H2": return 39
    elif card == "R1": return 5
    elif card == "NR": return next_rr(square)
    elif card == "NU": return next_util(square)
    elif card == "GB3": return (square - 3) % 40
    else: return square

def convert_communitychest(square, card):
    if card == "GO": return 0
    elif card == "JAIL": return 10
    else: return square

def draw_card(deck):
    card = deck.pop(0)
    deck.append(card)
    return card

def resolve_square_redirects(square,chance,community):
    #chance 7, 22, 36
    if square == 7 or square == 22 or square == 36:
        square = convert_chance(square, draw_card(chance))
    #community chests 2, 17, 33
    if square == 2 or square == 17 or square == 33:
        square = convert_communitychest(square, draw_card(community))
    #g2j 30
    if square == 30:
        return 10
    return square

def simulate(steps,sides):
    current_square = 0
    doubles = 0
    random.shuffle(_chance_deck)
    random.shuffle(_communitychest_deck)
    for step in range(steps):
        roll = dice_roll(sides)

        #count doubles
        if roll[0] == roll[1]: doubles += 1
        else: doubles = 0 

        #go to jail for triple doubles
        if doubles > 2:
            #jail
            doubles = 0
            current_square = 10 
        else:
            current_square = (current_square + roll[0] + roll[1]) % 40
            #resolve redirects
            current_square = resolve_square_redirects(current_square,_chance_deck,_communitychest_deck)

        #record end position
        _board[current_square] += 1

def modal_string(squares):
    modal_str = ''
    for square in squares:
        if len(square.__str__()) < 2:
            modal_str += "0" + square.__str__()
        else: modal_str += square.__str__()
    return modal_str

if __name__ == '__main__':

    stime = time.time()

    steps = 1000000
    simulate(steps,4)

    squares = list(_board.keys())
    squares.sort(key=lambda x:_board[x],reverse=True)

    print("Solution:{} Runtime:{}".format(modal_string(squares[0:3]),time.time()-stime))
