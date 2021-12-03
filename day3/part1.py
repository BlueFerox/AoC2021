# Advent of Code, Day 3, Part 1

testInput = '''\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
'''
testResult = 198

def solve(input):
    lines = [line for line in input.split('\n') if line != '']

    gamma = ''
    epsilon = ''

    for i in range(len(lines[0])):
        ones = sum(1 for line in lines if line[i] == '1')
        zeros = sum(1 for line in lines if line[i] == '0')
        gamma += '1' if ones > zeros else '0'
        epsilon += '1' if ones < zeros else '0'
    return int(gamma, 2) * int(epsilon, 2)


assert solve(testInput) == testResult

with open('day3/input.txt', 'r') as file:
    print(solve(file.read()))

