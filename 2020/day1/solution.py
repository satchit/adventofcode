import sys


def find_two_sum(l, total):
    d = set()
    for i in l:
        j = total - i
        if d and j in d:
            return i * j
        d.add(i)

def part1(l):
    return find_two_sum(l, 2020)
        

def part2(l):
    d = []
    for i in l:
        d.append(2020 - i)
    for idx, i in enumerate(l):
        tmp = l[idx]
        l[idx] = 0
        a = find_two_sum(l, d[idx])
        l[idx] = tmp
        if a:
            return a * l[idx]
    
        

if __name__ == '__main__':
    l = [int(i.strip()) for i in sys.stdin.readlines()]
    print part1(l)
    print part2(l)