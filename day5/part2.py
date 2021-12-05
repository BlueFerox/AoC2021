# Advent of Code, Day 5, Part 2

from collections import Counter
from itertools import chain
from typing import List, Tuple

testInput = '''\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''
testResult = 12

Coord = Tuple[int, ...]
Vent = Tuple[Coord, ...]

def parse(input: str) -> List[Vent]:
    return [tuple(tuple(int(n) for n in coord.split(',')) for coord in line.split(' -> ')) for line in input.split('\n') if line != '']

def isHorizontalOrVertical(vent: Vent) -> bool:
    return vent[0][0] == vent[1][0] or vent[0][1] == vent[1][1]

def isDiagonal(vent: Vent) -> bool:
    return abs(vent[0][0] - vent[1][0]) == abs(vent[0][1] - vent[1][1])

def sign(x: int) -> int:
    return -1 if x < 0 else (1 if x > 0 else 0)

def pointsBetween(vent: Vent) -> List[Coord]:
    direction = (sign(vent[1][0] - vent[0][0]), sign(vent[1][1] - vent[0][1]))
    return [(vent[0][0] + direction[0] * i, vent[0][1] + direction[1] * i) for i in range(max(abs(vent[0][0] - vent[1][0]), abs(vent[0][1] - vent[1][1])) + 1)]

def solve(input: str) -> int:
    return sum(1 for count in Counter(chain(*[pointsBetween(vent) for vent in parse(input) if isHorizontalOrVertical(vent) or isDiagonal(vent)])).values() if count >= 2)

assert solve(testInput) == testResult

with open('day5/input.txt', 'r') as file:
    print(solve(file.read()))

