# Advent of Code, Day 8, Part 1

from typing import List, Tuple


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
testResult = 26

Pattern = Tuple[str, ...]
Output = Tuple[str, ...]

def parse(input: str) -> List[Tuple[Pattern, Output]]:
    return [
        (tuple(line[0].split(' ')), tuple(line[1].split(' ')))
        for line
        in [line.split(' | ') for line in input.splitlines()]
        if line != '']

def solve(input):
    lines = parse(input)

    return sum(
        sum(1 for cs in output if len(cs) in [2, 3, 4, 7])
        for _, output
        in lines)

assert solve(testInput) == testResult

with open('day8/input.txt', 'r') as file:
    print(solve(file.read()))

