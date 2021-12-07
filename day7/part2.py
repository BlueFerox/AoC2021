# Advent of Code, Day 7, Part 2

testInput = '''\
16,1,2,0,4,2,7,1,2,14
'''
testResult = 168

def fuelFunc(n: int) -> int:
    return sum(range(1, n+1))

def solve(input):
    crabSubs = [int(line.strip()) for line in input.split(',') if line != '']

    fuel = list(enumerate(sum(fuelFunc(abs(n - crabSub)) for crabSub in crabSubs) for n in range(min(crabSubs), max(crabSubs)))).sort(key = lambda x: x[1])

    print(fuel)
    return 168

assert solve(testInput) == testResult

with open('day7/input.txt', 'r') as file:
    print(solve(file.read()))