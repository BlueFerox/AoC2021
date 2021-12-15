# Advent of Code, Day 15, Part 1

from collections import deque


TEST_INPUT = '''\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
'''
TEST_RESULT = 40

def adjacent(field, coord):
    x, y = coord
    return [
        (x + i, y + j)
        for i, j, in [(1, 0), (0, 1), (-1, 0), (0, -1)]
        if (x + i, y + j) in field
    ]

def solve(input):
    risks = dict()
    for y, line in enumerate(input.strip().splitlines()):
        for x, n in enumerate(line):
            risks[(x, y)] = int(n)
    maxX = max(x for x, _ in risks.keys())
    maxY = max(y for _, y in risks.keys())

    riskToPoint = {(0, 0): 0}
    todo = deque([(0, 0)])
    while todo:
        curr = todo.popleft()
        if curr == (maxX, maxY):
            continue

        for adj in adjacent(risks, curr):
            newRisk = riskToPoint[curr] + risks[adj]
            if adj not in riskToPoint or riskToPoint[adj] > newRisk:
                riskToPoint[adj] = newRisk
                todo.append(adj)
    return riskToPoint[(maxX, maxY)]
                
assert solve(TEST_INPUT) == TEST_RESULT

with open('day15/input.txt', 'r') as file:
    print(solve(file.read()))

