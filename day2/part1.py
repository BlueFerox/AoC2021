# Advent of Code, Day 2, Part 1

testInput = '''\
forward 5
down 5
forward 8
up 3
down 8
forward 2
'''
testResult = 150

def solve(input):
    lines = [line.split(' ') for line in input.split('\n') if line != '']
    operations = [(line[0], int(line[1])) for line in lines]
    
    horizontal = 0
    depth = 0
    for op, n in operations:
        if op == "forward":
            horizontal += n
        elif op == 'up':
            depth -= n
        elif op == 'down':
            depth += n

    return horizontal * depth

assert solve(testInput) == testResult

with open('day2/input.txt', 'r') as file:
    print(solve(file.read()))
    
