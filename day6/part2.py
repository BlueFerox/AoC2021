# Advent of Code, Day 6, Part 1

from collections import Counter, defaultdict
from functools import reduce
from typing import Dict, List


testInput = '''\
3,4,3,1,2
'''
testResult = 26984457539

def nextDay(lanternSchool: Dict[int, int]):
    nextLanternSchool = defaultdict(lambda: 0)

    for fishAge in lanternSchool.keys():
        if fishAge == 0:
            nextLanternSchool[8] += lanternSchool[0]
            nextLanternSchool[6] += lanternSchool[0]
        else:
            nextLanternSchool[fishAge - 1] += lanternSchool[fishAge]
    return nextLanternSchool

def solve(input: str) -> int:
    fishes: Dict[int, int] = Counter(
        int(line.strip())
        for line
        in input.split(',')
        if line != '')

    for _ in range(256):
        fishes = nextDay(fishes)
    return sum(fishes.values())

assert solve(testInput) == testResult

with open('day6/input.txt', 'r') as file:
    print(solve(file.read()))

