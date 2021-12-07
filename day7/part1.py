# Advent of Code, Day 7, Part 1

from statistics import median

testInput = '''\
16,1,2,0,4,2,7,1,2,14
'''
testResult = 37

def solve(input):
    crabSubs = [int(line.strip()) for line in input.split(',') if line != '']
    horizontalPos = int(median(crabSubs))
    fuel = sum(abs(horizontalPos - crabSub) for crabSub in crabSubs)
    return fuel
assert solve(testInput) == testResult

with open('day7/input.txt', 'r') as file:
    print(solve(file.read()))

