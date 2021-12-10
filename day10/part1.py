# Advent of Code, Day 10, Part 1

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
testResult = 26397

def solve(input):
    lines = [line for line in input.splitlines() if line != '']

    chunkChars = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    
    pointsPerChar = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    points = 0
    for line in lines:
        stack = []
        for c in line:
            if c in chunkChars:
                stack.append(c)
            elif c == chunkChars[stack[-1]]:
                stack.pop()
            else:
                points += pointsPerChar[c]
                break

    return points


assert solve(testInput) == testResult

with open('day10/input.txt', 'r') as file:
    print(solve(file.read()))

