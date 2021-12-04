# Advent of Code, Day 4, Part 2

from dataclasses import dataclass
from typing import List

testInput = '''\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''
testResult = 1924

@dataclass
class BingoNum:
    n: int
    marked: bool

    def __repr__(self):
        if self.marked:
            return 'x'
        return str(self.n)

@dataclass
class BingoField:
    field: List[List[BingoNum]]
    hasWon: bool

def hasWon(field):
    rowVictory = any(all(bn.marked for bn in field[i]) for i in range(5)) 
    colVictory = any(all(bn.marked for bn in list(zip(*field))[i]) for i in range(5))
    return rowVictory or colVictory

def solve(input):
    blocks = [line for line in input.replace('  ', ' ').replace('\n ', '\n').split('\n\n')]
    pickedInts = [int(n) for n in blocks[0].split(',')]
    
    winningFields = list()

    bfields = [BingoField([[BingoNum(int(n), False) for n in line.split(' ')] for line in block.split('\n') if line != ''], False) for block in blocks[1:]]
    for picked in pickedInts:
        for bfield in bfields:
            if not bfield.hasWon:
                for line in bfield.field:
                    for bn in line:
                        if bn.n == picked and (not bn.marked):
                            bn.marked = True
                if hasWon(bfield.field):
                    winningFields.append(picked * sum(sum(bn.n for bn in line if not bn.marked) for line in bfield.field))
                    bfield.hasWon = True
                    print(bfield.field)
    return winningFields.pop()

assert solve(testInput) == testResult

with open('day4/input.txt', 'r') as file:
    print(solve(file.read()))
    pass

