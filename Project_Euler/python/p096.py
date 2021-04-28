import os
import time

"""
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept.
Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares.
The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9.
Below is an example of a typical starting puzzle grid and its solution grid.
p096_1.png     p096_2.png

A well constructed Su Doku puzzle has a unique solution and can be solved by logic,
although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). 
The complexity of the search determines the difficulty of the puzzle;
the example above is considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty,
but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid;
for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
"""
#brute force solve
def check_row(puzzle,row):
    return set(puzzle[row])

def check_column(puzzle,column):
    values = set()
    for i in range(9):
        values.add(puzzle[i][column])
    return values

def check_sector(puzzle,row,column):
    row_sector = row//3
    column_sector = column//3
    values = set()
    for row in range(3):
        for column in range(3):
            values.add(puzzle[row+(3*row_sector)][column+(3*column_sector)])
    return values

def valid_values(puzzle,row,column):
    values = set(range(1,10))
    values = values.difference(check_row(puzzle,row))
    values = values.difference(check_column(puzzle,column))
    values = values.difference(check_sector(puzzle,row,column))
    return values

def solve(puzzle):
    def delver(puzzle,row,column):
        #entered final valid value
        if row > 8:
            return puzzle

        next_column = (column+1) % 9
        next_row = row
        if next_column == 0:
            next_row += 1 

        if puzzle[row][column] != 0:
            return delver(puzzle,next_row,next_column)

        values = valid_values(puzzle,row,column)
        while len(values) > 0:
            value = values.pop()
            puzzle[row][column] = value
            solution = delver(puzzle,next_row,next_column)
            if not solution is None:
                return solution
            puzzle[row][column] = 0
        return None

    #find starting point
    found = False
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == 0:
                found = True
                break
        if found:
            break
    return delver(puzzle,row,column)

def stringify(puzzle):
    string = ''
    for digit in puzzle[0][:3]:
        string += str(digit)
    return string

if __name__ == '__main__':

    stime = time.time()

    line_number = int(0)
    total = int(0)
    puzzle = []
    with open("Project_Euler\python\data\p096_sudoku.txt") as data:
        while True:
            line_number = line_number % 10
            if line_number:
                puzzle.append([])
                for digit in data.readline().strip('\n'):
                    puzzle[line_number-1].append(int(digit))
            else:
                if not puzzle == []:
                    total += int(stringify(solve(puzzle)))
                if data.readline() == '':
                    break
                puzzle = []
            line_number += 1
    print("Solution:{} Runtime:{}".format(total,time.time()-stime))
