# Advent of Code, Day 12, Part 1

from collections import defaultdict

TEST_INPUT = '''\
start-A
start-b
A-c
A-b
b-d
A-end
b-end
'''
TEST_RESULT = 10

START = 'start'
END = 'end'

def paths(conns, path: list[str]) -> list[list[str]]:
    lastCave = path[-1]
    if lastCave == END:
        return [path]
    allPaths = []
    for cave in conns[lastCave]:
        if not (cave.islower() and cave in path):
            nextPath = path[:]
            nextPath.append(cave)
            nps = paths(conns, nextPath)
            if nps != []:
                allPaths.extend(nps)
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

