# Advent of Code, Day 11, Part 1

from collections import defaultdict
from sys import maxsize
from typing import Set, Tuple
testInput = '''\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''
testResult = 1656

def adj(x, y):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if not 0 == i == j:
                yield x + i, y + j

def flash(octopi, flashQueue: Set[Tuple[int, int]]):
    hasFlashed = set()
    while len(flashQueue) > 0:
        oct = flashQueue.pop()
        for adjOct in adj(oct[0], oct[1]):
            if adjOct in octopi:
                octopi[adjOct] += 1
                hasFlashed.add(oct)
                if octopi[adjOct] > 9 and not adjOct in hasFlashed:
                    flashQueue.add(adjOct)

    for oct in hasFlashed:
        octopi[oct] = 0

    return len(hasFlashed)

def solve(input):
    octopi = {
        (x, y): int(n)
        for y, row in enumerate(input.splitlines())
        for x, n in enumerate(row)}
    sum = 0
    for _ in range(100):
        for oct in octopi.keys():
            octopi[oct] += 1
        sum += flash(octopi, set(oct for oct in octopi.keys() if octopi[oct] > 9))
    return sum
            






        

assert solve(testInput) == testResult

with open('day11/input.txt', 'r') as file:
    print(solve(file.read()))

