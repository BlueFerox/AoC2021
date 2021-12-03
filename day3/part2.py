# Advent of Code, Day 3, Part 2

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
testResult = 230

def solve(input):
    lines = [line for line in input.split('\n') if line != '']

    def searchForRating(bitCriteria):
        remLines = lines

        for i in range(len(lines[0])):
            ones = sum(1 for line in remLines if line[i] == '1')
            zeros = sum(1 for line in remLines if line[i] == '0')
            maxBit = '1' if bitCriteria(ones, zeros) else '0'
            
            remLines = [line for line in remLines if line[i] == maxBit]
            
            if len(remLines) == 1:
                return int(remLines[0], 2)
    
    oxygen = searchForRating(lambda ones, zeros: ones >= zeros)
    co2 = searchForRating(lambda ones, zeros: ones < zeros)
    return oxygen * co2


assert solve(testInput) == testResult

with open('day3/input.txt', 'r') as file:
    print(solve(file.read()))

