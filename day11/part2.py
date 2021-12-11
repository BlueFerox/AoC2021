# Advent of Code, Day 11, Part 2

TEST_INPUT = '''\
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
TEST_RESULT = 195

MAX_STEPS: int = 1000
ROWS: int = 10
COLS: int = 10
FLASH_ENERGY = 9

def adj(x: int, y: int) -> list[tuple[int, int]]:
    return [(x + i, y + j)
        for i in [-1, 0, 1]
        for j in [-1, 0, 1]
        if not 0 == i == j]

def flash(octopi, flashQueue: set[tuple[int, int]]):
    hasFlashed = set()
    while len(flashQueue) > 0:
        oct = flashQueue.pop()
        for adjOct in adj(oct[0], oct[1]):
            if adjOct in octopi:
                octopi[adjOct] += 1
                hasFlashed.add(oct)
                if octopi[adjOct] > FLASH_ENERGY and not adjOct in hasFlashed:
                    flashQueue.add(adjOct)   

    for oct in hasFlashed:
        octopi[oct] = 0
    return len(hasFlashed)

def solve(input):
    octopi = {
        (x, y): int(n)
        for y, row in enumerate(input.splitlines())
        for x, n in enumerate(row)}

    for step in range(MAX_STEPS):
        for y in range(ROWS):
            for x in range(COLS):
                octopi[(x, y)] += 1
        
        if flash(octopi, set(oct for oct in octopi.keys() if octopi[oct] > FLASH_ENERGY)) >= ROWS * COLS:
            return step + 1
    raise Exception(f'Octupi do not synchronise in {MAX_STEPS} steps.')

assert solve(TEST_INPUT) == TEST_RESULT

with open('day11/input.txt', 'r') as file:
    print(solve(file.read()))

