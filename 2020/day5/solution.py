import sys

def parse_input(text):
    return [i.strip() for i in text.splitlines()]

def bisect(i, j):
    return (i + j) / 2

def find_seat(data):
    r = data[:7]
    c = data[7:]
    i, j = 0, 127
    for char in r:
        row = bisect(i, j)
        if char == 'F':
            j = row
        else:
            i = row + 1
        if i == j:
            row = i
            break
    i, j = 0, 7
    for char in c:
        col = bisect(i, j)
        if char == 'L':
            j = col
        else:
            i = col + 1
        if i == j:
            col = i
            break
    return row * 8 + col

def part1(data):
    return max(find_seat(code) for code in data)

def part2(data):
    seats = [find_seat(code) for code in data]
    seats.sort()
    missing = None
    for i in seats:
        if i + 1 not in seats and i + 2 in seats:
            return i + 1

if __name__ == '__main__':
    data = parse_input(sys.stdin.read())
    print part1(data)
    print part2(data)
