# Advent of Code, Day 7, Part 2

testInput = '''\
16,1,2,0,4,2,7,1,2,14
'''
testResult = 168

def tri(a: int, b: int) -> int:
    n = abs(a - b)
    return (n*(n+1)) // 2

def solve(input):
    crabs = [
        int(line.strip())
        for line
        in input.split(',')
        if line != '']

    return min(
        sum(tri(n, crab) for crab in crabs)
        for n
        in range(min(crabs), max(crabs) + 1))

assert solve(testInput) == testResult

with open('day7/input.txt', 'r') as file:
    print(solve(file.read()))