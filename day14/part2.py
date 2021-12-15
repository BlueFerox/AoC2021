# Advent of Code, Day 14, Part 2

from collections import Counter
from math import ceil

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
TEST_RESULT = 2188189693529

def solve(input):
    template, rules_s = input.split('\n\n')

    rules = dict()
    elems = set(template)
    for line in rules_s.splitlines():
        elemPair, insertElem = line.split(' -> ')
        rules[(elemPair[0], elemPair[1])] = [(elemPair[0], insertElem), (insertElem, elemPair[1])]
        elems.add(insertElem)
    
    polymerPairs = Counter(
        (template[i], template[i + 1])
        for i
        in range(len(template) - 1))

    for step in range(40):
        nextPolymer = Counter()
        for elemPair in polymerPairs.keys():
            for newPair in rules[elemPair]:
                nextPolymer[newPair] += polymerPairs[elemPair]
        polymerPairs = nextPolymer

    elemsCounter = Counter()
    for elem in elems:
        elemsCounter[elem] = sum(
            count
            for polyPair, count
            in polymerPairs.items()
            if polyPair[0] == elem
        )
    elemsCounter[template[-1]] += 1
    mostCommon = elemsCounter.most_common()
    return mostCommon[0][1] - mostCommon[-1][1]   
        

assert solve(TEST_INPUT) == TEST_RESULT

with open('day14/input.txt', 'r') as file:
    print(solve(file.read()))

