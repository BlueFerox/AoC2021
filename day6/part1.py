# Advent of Code, Day 6, Part 1

from collections import Counter, defaultdict
from functools import reduce
from typing import Dict, List


testInput = '''\
3,4,3,1,2
'''
testResult = 5934

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
    lanternSchool = Counter(int(line.strip()) for line in input.split(',') if line != '')

    print(f'Initial state: {lanternSchool.items()}')
    for day in range(80):
        lanternSchool = nextDay(lanternSchool)
        print(f'Day {day+1}: {lanternSchool.items()}')
    return sum(lanternSchool.values())

assert solve(testInput) == testResult

with open('day6/input.txt', 'r') as file:
    print(solve(file.read()))

