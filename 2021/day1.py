import sys

data = [int(i.strip()) for i in open('inputs/day1.txt').readlines()]

def part1():
    increments = 0
    for c, n in zip(data[:-1], data[1:]):
        if n > c:
            increments += 1
    return increments

def part2():
    increments = 0
    prev = sum(data[:3])
    for idx in range(1, len(data) - 2):
        curr = sum(data[idx:idx+3])
        if curr > prev:
            increments += 1
        prev = curr
    return increments

if __name__ == '__main__':
    print(part1())
    print(part2())