# Advent of Code, Day 9, Part 1

from typing import List, Tuple


testInput = '''\
2199943210
3987894921
9856789892
8767896789
9899965678
'''
testResult = 15

Coord = Tuple[int, int]

def parse(input: str) -> List[List[int]]:
    return [
        [int(c) for c in line]
        for line
        in input.splitlines()
        if line != ''
    ]

def adjacent(ns: List[List[int]], i: int, j: int) -> List[Coord]:
    return [
        (i + i_o, j + j_o)
        for i_o, j_o
        in [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if 0 <= i + i_o < len(ns) and 0 <= j + j_o < len(ns[i + i_o])]

def isLowPoint(ns: List[List[int]], i: int, j: int) -> bool:
    return all(
        ns[adjI][adjJ] > ns[i][j]
        for adjI, adjJ
        in adjacent(ns, i, j))

def solve(input):
    ns: List[List[int]] = parse(input)
    return sum(
        n + 1
        for i, row in enumerate(ns)
        for j, n in enumerate(row)
        if isLowPoint(ns, i, j))

assert solve(testInput) == testResult

with open('day9/input.txt', 'r') as file:
    print(solve(file.read()))

