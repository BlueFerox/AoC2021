# Advent of Code, Day 16, Part 2

from functools import reduce
from operator import mul



operations = {
    0: sum,
    1: lambda ns: reduce(mul, ns, 1),
    2: min,
    3: max,
    4: lambda ns: ns[0],
    5: lambda ns: 1 if ns[0] > ns[1] else 0,
    6: lambda ns: 1 if ns[0] < ns[1] else 0,
    7: lambda ns: 1 if ns[0] == ns[1] else 0
}

def parseLiteral(message: str):
    literalBits = ''
    while message[0] == '1':
        literalBits += message[1:5]
        message = message[5:]
    literalBits += message[1:5]
    return int(literalBits, 2), message[5:]

def parsePacket(message: str):
    typeId = int(message[3:6], 2)
    ns = []
    if typeId == 4:
        literal, remainder = parseLiteral(message[6:])
        ns.append(literal)

    elif message[6] == '0':
        offset = int(message[7:22], 2)
        subpacket = message[22:22 + offset]
        while subpacket:
            subpacket, n = parsePacket(subpacket)
            ns.append(n)
        remainder = message[22 + offset:]
    
    elif message[6] == '1':
        subpacketCount = int(message[7:18], 2)  
        remainder = message[18:]
        for i in range(subpacketCount):
            remainder, n = parsePacket(remainder)
            ns.append(n)

    return remainder, operations[typeId](ns)


def solve(input):
    message = ''.join(f'{int(h, 16):04b}' for h in input.strip())
    return parsePacket(message)[1]


assert solve('C200B40A82') == 3
assert solve('04005AC33890') == 54
assert solve('880086C3E88112') == 7
assert solve('CE00C43D881120') == 9
assert solve('D8005AC2A8F0') == 1
assert solve('F600BC2D8F') == 0
assert solve('9C005AC2F8F0') == 0
assert solve('9C0141080250320F1802104A08') == 1

with open('day16/input.txt', 'r') as file:
    print(solve(file.read()))

