# Advent of Code, Day 1, Part 2

testInput = '''\
199
200
208
210
200
207
240
269
260
263
'''
testResult = 5

def solve(input):
    lines = [int(line) for line in input.split('\n') if line != '']

    counter = 0

    for i, n in enumerate(lines[:-3]):
        if lines[i + 3] > n:
            counter += 1
    return counter

assert solve(testInput) == testResult

with open('day1/input.txt', 'r') as file:
   print(solve(file.read()))

