# Advent of Code, Day 2, Part 2

testInput = '''\
forward 5
down 5
forward 8
up 3
down 8
forward 2
'''
testResult = 900

def solve(input):
    lines = [line.split(' ') for line in input.split('\n') if line != '']
    operations = [(line[0], int(line[1])) for line in lines]
    
    horizontal = 0
    depth = 0
    aim = 0

    for op, n in operations:
        if op == "forward":
            horizontal += n
            depth += aim * n
        elif op == 'up':
            aim -= n
        elif op == 'down':
            aim += n

    return horizontal * depth

assert solve(testInput) == testResult

with open('day2/input.txt', 'r') as file:
    print(solve(file.read()))

