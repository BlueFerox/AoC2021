# Advent of Code, Day 15, Part 2

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
TEST_RESULT = 315

def adjacent(field, coord):
    x, y = coord
    return [
        ((x + i, y + j), dir)
        for i, j, dir in [(1, 0, 'l'), (0, 1, 'u'), (-1, 0, 'r'), (0, -1, 'd')]
        if (x + i, y + j) in field
    ]

def riskLevel(n):
    return n % 9 + 1

def solve(input):
    risksPattern = dict()
    for y, line in enumerate(input.strip().splitlines()):
        for x, n in enumerate(line):
            risksPattern[(x, y)] = int(n) - 1
    maxX = max(x for x, _ in risksPattern.keys()) + 1
    maxY = max(y for _, y in risksPattern.keys()) + 1

    risks = dict()
    for tileRow in range(5):
        for tileCol in range(5):
            for x, y in risksPattern.keys():
                risks[(x + maxX * tileCol, y + maxY * tileRow)] = riskLevel(risksPattern[(x, y)] + tileRow + tileCol)
    print(maxX, maxY)
    maxX *= 5
    maxY *= 5
    # for y in range(maxY):
    #     for x in range(maxX):
    #         print(risks[(x, y)], end='')
    #     print()


    riskToPoint = {(0, 0): (0, None, True)}
    todo = deque([(0, 0)])
    while todo:
        curr = todo.popleft()
        if curr == (maxX, maxY):
            continue

        for adj, dir in adjacent(risks, curr):
            newRisk = riskToPoint[curr][0] + risks[adj]
            if adj not in riskToPoint or riskToPoint[adj][0] > newRisk:
                riskToPoint[adj] = (newRisk, curr, False)
                todo.append(adj)
        #print(len(todo))
    c = (maxX - 1, maxY - 1)

    while c != (0, 0):
        risk, prev, marked = riskToPoint[c]
        riskToPoint[c] = (risk, prev, True)
        c = prev
    
    for y in range(maxY):
        for x in range(maxX):
            if riskToPoint[(x, y)][2]:
                print(f'\033[94m{risks[(x, y)]}\033[00m', end='')
            else:
                print(risks[(x, y)], end='')
        print()
    print('END', riskToPoint[(maxX -1, maxY - 1)])
    print(maxX, maxY)
    return riskToPoint[(maxX - 1, maxY - 1)][0]

assert solve(TEST_INPUT) == TEST_RESULT

with open('day15/input.txt', 'r') as file:
    print(solve(file.read()))

