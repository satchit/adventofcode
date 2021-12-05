import sys
import collections

def parse(txt):
    return [line.strip() for line in txt.splitlines()]

test_data = parse('''00100
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
01010''')

data = parse(open('inputs/day3.txt').read())

def part1(data):
    gamma, epsilon = [], []
    for col in zip(*data):
        c = collections.Counter(col).most_common()
        gamma.append(c[0][0])
        epsilon.append(c[1][0])
    return int(''.join(gamma), 2) * int(''.join(epsilon), 2)
        


def part2(data):
    oxygen, scrubber = data[:], data[:] 
    oxygen_rating = scrubber_rating = None
    for idx in range(len(data[0])):
        if len(oxygen) > 1:
            c = collections.Counter([x[idx] for x in oxygen])
            if c['0'] == c['1']:
                o = '1'
            else:
                o = c.most_common()[0][0]
            oxygen = [x for x in oxygen if x[idx] == o]
        if len(scrubber) > 1:
            c = collections.Counter([x[idx] for x in scrubber])
            if c['0'] == c['1']:
                s = '0'
            else:
                s = c.most_common()[1][0]
            scrubber = [x for x in scrubber if x[idx] == s]
            
    oxygen_rating = int(oxygen[0], 2)
    scrubber_rating = int(scrubber[0], 2)
    return oxygen_rating * scrubber_rating

if __name__ == '__main__':
    print(part1(data))
    print(part2(data))