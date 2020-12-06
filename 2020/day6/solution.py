import sys
import functools

def parse_input(text):
    groups = []
    group = []
    for line in text.splitlines():
        if line.strip():
            group.append(list(line.strip()))
        else:
            groups.append(group)
            group = []
    if group:
        groups.append(group)
    return groups

def part1(groups):
    return sum([len(set(sum(group, []))) for group in groups])

def part2(groups):
    total = 0
    return sum(
        len(functools.reduce(set.intersection, [set(answer) for answer in group])) 
        for group in groups)
        

if __name__ == '__main__':
    groups = parse_input(sys.stdin.read())
    print part1(groups)
    print part2(groups)