# Advent of Code, Day 13, Part 2

from functools import reduce

TEST_INPUT = '''\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
'''
TEST_RESULT = None

def doFold(dots: set[tuple[int, int]], fold: tuple[str, int]) -> set[tuple[int, int]]:
    if fold[0] == 'y':
        return doUpFold(dots, fold[1])
    elif fold[0] == 'x':
        return doLeftFold(dots, fold[1])
    else:
        raise Exception(f'Invalid fold found: {fold}')

def doUpFold(dots: set[tuple[int, int]], foldY: int) -> set[tuple[int, int]]:
    return set((x, y) for x, y in dots if y < foldY).union((x, foldY - (y - foldY)) for x, y in dots if y > foldY)

def doLeftFold(dots: set[tuple[int, int]], foldX: int) -> set[tuple[int, int]]:
    return set((x, y) for x, y in dots if x < foldX).union((foldX - (x - foldX), y) for x, y in dots if x > foldX)

def printDots(dots: set[tuple[int, int]]) -> None:
    maxX = max(x for x, _ in dots)
    maxY = max(y for _, y in dots)
    for y in range(maxY + 1):
        for x in range(maxX + 1):
            if (x, y) in dots:
                print('#', end='')
            else:
                print(' ', end='')
        print()

def parse(input: str) -> tuple[set[tuple[int, int]], list[tuple[str, int]]]:
    dots_s, folds_s = input.strip().split('\n\n')
    dots = set()
    for dot in dots_s.splitlines():
        x, y = dot.split(',')
        dots.add((int(x), int(y)))

    folds = []
    for fold in folds_s.splitlines():
        folds.append((
            'x' if 'x' in fold else 'y',
            int(fold.split('=')[-1])))
    return dots, folds

def solve(input: str):
    dots, folds = parse(input)

    dots = reduce(doFold, folds, dots)
    printDots(dots)

assert solve(TEST_INPUT) == TEST_RESULT

with open('day13/input.txt', 'r') as file:
    print(solve(file.read()))

