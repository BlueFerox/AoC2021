# Advent of Code, Day 11, Part 1

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
TEST_RESULT = 1656

STEPS: int = 100
FLASH_ENERGY = 9

def adj(x: int, y: int) -> list[tuple[int, int]]:
    return [(x + i, y + j)
        for i in [-1, 0, 1]
        for j in [-1, 0, 1]
        if not 0 == i == j]

def flash(octopi: dict[tuple[int, int], int], flashQueue: set[tuple[int, int]]) -> int:
    hasFlashed: set[tuple[int, int]] = set()
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

def solve(input: str) -> int:
    octopi = {
        (x, y): int(n)
        for y, row in enumerate(input.splitlines())
        for x, n in enumerate(row)}

    sum: int = 0
    for _ in range(STEPS):
        for oct in octopi.keys():
            octopi[oct] += 1
        sum += flash(octopi, set(oct for oct in octopi.keys() if octopi[oct] > FLASH_ENERGY))
    return sum

assert solve(TEST_INPUT) == TEST_RESULT

with open('day11/input.txt', 'r') as file:
    print(solve(file.read()))

