import sys
from pathlib import Path

def main():

    if not len(sys.argv) == 2:
        print('usage: setupDay.py <day_number>')
        exit()
    
    day = sys.argv[1]
    
    Path(f'day{day}').mkdir(exist_ok=True)
    for part in [1, 2]:
        with Path(f'day{day}/part{part}.py').open('w') as file:
            file.write(f'''\
# Advent of Code, Day {day}, Part {part}

testInput = \'\'\'\\

\'\'\'
testResult = None

def solve(input):
    pass

assert solve(testInput) == testResult

with open(\'day{day}/input.txt\', \'r\') as file:
    print(solve(file.read()))

''')

if __name__ == '__main__':
    main()
    raise SystemExit()