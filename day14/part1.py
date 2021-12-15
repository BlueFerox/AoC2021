# Advent of Code, Day 14, Part 1

from collections import Counter


TEST_INPUT = '''\
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
'''
TEST_RESULT = 1588

def solve(input):
    template, rules_s = input.split('\n\n')

    rules = dict()
    for line in rules_s.splitlines():
        pairElems, insertElem = line.split(' -> ')
        rules[(pairElems[0], pairElems[1])] = insertElem

    polymer = template
    for step in range(10):
        polymer = ''.join(
            f'{polymer[i]}{rules[(polymer[i], polymer[i + 1])]}'
            for i
            in range(len(polymer) - 1)
        ) + polymer[-1]

    mostCommon = Counter(polymer).most_common()
    return mostCommon[0][1] - mostCommon[-1][1]





assert solve(TEST_INPUT) == TEST_RESULT

with open('day14/input.txt', 'r') as file:
    print(solve(file.read()))

