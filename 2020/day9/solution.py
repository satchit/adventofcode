import re
import sys

def find_two_sum(l, total):
    seen = set()
    for i in l:
        j = total - i
        if seen and j in seen:
            return i, j
        seen.add(i)

def part1(data, delta):
    idx = delta
    while idx < len(data):
        l = data[idx-delta:idx]
        i = find_two_sum(l, data[idx])
        if i is None:
            return data[idx]
        idx += 1

def part2(data, total):
    for delta in range(2, len(data)):
        for idx in range(0, len(data) - delta):
            l = data[idx:idx+delta]
            if sum(l) == total:
                return min(l) + max(l)

        
if __name__ == '__main__':
    data = [int(line.strip()) for line in sys.stdin.readlines()]
    invalid = part1(data, 25)
    print invalid
    print part2(data, invalid)
