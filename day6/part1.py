# Advent of Code, Day 6, Part 1

from collections import Counter, defaultdict
from typing import Dict


testInput = '''\
3,4,3,1,2
'''
testResult = 5934

def nextDay(fishes: Dict[int, int]):
    nextFishes = defaultdict(lambda: 0)

    for n in fishes.keys():
        if n == 0:
            nextFishes[8] += fishes[0]
            nextFishes[6] += fishes[0]
        else:
            nextFishes[n - 1] += fishes[n]
    return nextFishes

def solve(input: str) -> int:
    fishes: Dict[int, int] = Counter(
        int(line.strip())
        for line
        in input.split(',')
        if line != '')

    for _ in range(80):
        fishes = nextDay(fishes)
    return sum(fishes.values())

assert solve(testInput) == testResult

with open('day6/input.txt', 'r') as file:
    print(solve(file.read()))

