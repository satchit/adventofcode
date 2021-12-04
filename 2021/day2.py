import sys

def parse(txt):
    return [[c.strip() for c in line.strip().split()] for line in txt.splitlines()]

test_data = parse('''forward 5
down 5
forward 8
up 3
down 8
forward 2''')

data = parse(open('inputs/day2.txt').read())

def part1(data):
    pos = [0, 0]
    for dir, delta in data:
        if dir == 'forward':
            pos[0] += int(delta)
        elif dir == 'up':
            pos[1] -= int(delta)
        elif dir == 'down':
            pos[1] += int(delta)
    return pos[0] * pos[1]


def part2(data):
    aim = 0
    pos = [0, 0]
    for dir, delta in data:
        if dir == 'forward':
            pos[0] += int(delta)
            pos[1] += aim * int(delta)
        elif dir == 'up':
            aim -= int(delta)
        elif dir == 'down':
            aim += int(delta)
    return pos[0] * pos[1]

if __name__ == '__main__':
    print(part1(data))
    print(part2(data))