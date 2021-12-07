# Advent of Code, Day 7, Part 1

from statistics import median

testInput = '''\
16,1,2,0,4,2,7,1,2,14
'''
testResult = 37

def solve(input):
    crabs = [
        int(line.strip())
        for line
        in input.split(',')
        if line != '']

    return sum(
        abs(int(median(crabs)) - crabSub) 
        for crabSub
        in crabs)

assert solve(testInput) == testResult

with open('day7/input.txt', 'r') as file:
    print(solve(file.read()))

