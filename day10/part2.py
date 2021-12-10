# Advent of Code, Day 10, Part 2

from statistics import median
from typing import List, Optional

testInput = '''\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''
testResult = 288957

chunkChars = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
pointsPerChar = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
def fixLine(line: str) -> Optional[str]:
    stack = []
    for c in line:
        if c in chunkChars:
            stack.append(c)
        elif c == chunkChars[stack[-1]]:
            stack.pop()
        else:
            return

    stack.reverse()
    return ''.join(chunkChars[c] for c in stack)


def solve(input):
    lines = [line for line in input.splitlines() if line != '']

    scores = []
    for line in lines:
        score = 0
        fixed = fixLine(line)
        if fixed:
            for c in fixed:
                score *= 5
                score += pointsPerChar[c]
            scores.append(score)
    
    return median(scores)
    


assert solve(testInput) == testResult

with open('day10/input.txt', 'r') as file:
    print(solve(file.read()))

