# Advent of Code, Day 8, Part 2

from typing import Dict, List, Tuple
from collections import Counter


testInput = '''\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
'''
testResult = 61229

Pattern = Tuple[str, ...]
Output = Tuple[str, ...]

def parse(input: str) -> List[Tuple[Pattern, Output]]:
    return [
        (tuple(line[0].split(' ')), tuple(line[1].split(' ')))
        for line
        in [line.split(' | ') for line in input.splitlines()]
        if line != '']

def eq(x: str, y: str) -> bool:
    all(c in x for c in y)

def solve(input):
    lines = parse(input)

    sum = 0
    for pattern, outout in lines:
        segKnown: Dict[str, str] = dict()
        nKnown: Dict[int, str] = dict()

        for key, count in Counter(''.join(pattern)).items():
            if count == 6:
                segKnown['b'] = key
            if count == 4:
                segKnown['e'] = key
            if count == 9:
                segKnown['f'] = key

        for s in pattern:
            if len(s) == 2:   nKnown[1] = s
            elif len(s) == 4: nKnown[4] = s
            elif len(s) == 3: nKnown[7] = s
            elif len(s) == 7: nKnown[8] = s

        for char in nKnown[1]:
            if char not in segKnown.values():
                segKnown['c'] = char
        
        for char in nKnown[7]:
            if char not in segKnown.values():
                segKnown['a'] = char

        for char in nKnown[4]:
            if char not in segKnown.values():
                segKnown['d'] = char
        
        for char in nKnown[8]:
            if char not in segKnown.values():
                segKnown['g'] = char

        nKnown[0] = ''.join(segKnown[c] for c in 'abcefg')
        nKnown[2] = ''.join(segKnown[c] for c in 'acdeg')
        nKnown[3] = ''.join(segKnown[c] for c in 'acdfg')
        nKnown[5] = ''.join(segKnown[c] for c in 'abdfg')
        nKnown[6] = ''.join(segKnown[c] for c in 'abdefg')
        nKnown[9] = ''.join(segKnown[c] for c in 'abcdfg')

        ns = [] 
        for o in outout:
            for i in range(10):
                if sorted(o) == sorted(nKnown[i]):
                    ns.append(str(i))
        sum += int(''.join(ns))
    return sum       

assert solve(testInput) == testResult

with open('day8/input.txt', 'r') as file:
    print(solve(file.read()))

