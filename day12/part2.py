# Advent of Code, Day 12, Part 2

from collections import defaultdict
from typing import Counter


TEST_INPUT = '''\
start-A
start-b
A-c
A-b
b-d
A-end
b-end
'''
TEST_RESULT = 36

START = 'start'
END = 'end'

def isValidNextCave(path, cave):
    if cave.islower() and cave in path and cave != START:
        counter = Counter(c for c in path if c.islower() and c != START)
        #print(counter)
        return counter.most_common(1).pop()[1] < 2
    return cave != START


def paths(conns, path: list[str]) -> list[list[str]]:
    lastCave = path[-1]
    if lastCave == END:
        return [path]
    allPaths = []
    for cave in conns[lastCave]:
        if isValidNextCave(path, cave):
            nextPath = path[:]
            nextPath.append(cave)
            nps = paths(conns, nextPath)
            if nps != []:
                allPaths.extend(nps)
    #print(allPaths)
    return allPaths


def solve(input):
    lines = [line.split('-') for line in input.splitlines() if line != '']
    
    conns = defaultdict(lambda: [])
    for line in lines:
        conns[line[0]].append(line[1])
        conns[line[1]].append(line[0])

    allPaths = paths(conns, [START])
    return len(allPaths)

assert solve(TEST_INPUT) == TEST_RESULT

with open('day12/input.txt', 'r') as file:
    print(solve(file.read()))

