# Advent of Code, Day 16, Part 1

TEST_INPUT = '''\
A0016C880162017C3686B18A3D4780
'''
TEST_RESULT = 31

def parseLiteral(message: str):
    literalBits = ''
    while message[0] == '1':
        literalBits += message[1:5]
        message = message[5:]
    literalBits += message[1:5]
    return int(literalBits, 2), message[5:]

def parsePacket(message: str):
    version = int(message[:3], 2)
    typeId = int(message[3:6], 2)
    versionSum = 0
    if typeId == 4:
        literal, remainder = parseLiteral(message[6:])

    elif message[6] == '0':
        offset = int(message[7:22], 2)
        subpacket = message[22:22 + offset]
        while subpacket:
            subpacket, subVersion = parsePacket(subpacket)
            versionSum += subVersion
        remainder = message[22 + offset:]
    
    elif message[6] == '1':
        subpacketCount = int(message[7:18], 2)  
        remainder = message[18:]
        for i in range(subpacketCount):
            remainder, subVersion = parsePacket(remainder)
            versionSum += subVersion
    return remainder, version + versionSum
    

def solve(input):
    message = ''.join(f'{int(h, 16):04b}' for h in input.strip())
    
    return parsePacket(message)[1]


assert solve(TEST_INPUT) == TEST_RESULT

with open('day16/input.txt', 'r') as file:
    print(solve(file.read()))

