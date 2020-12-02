import sys

def validate_entry_part1(entry):
    rule, password = [i.strip() for i in entry.split(':')]
    _range, char = rule.split(' ')
    _min, _max = [int(i) for i in _range.split('-')]
    occurrences = password.count(char)
    return _min <= occurrences and occurrences <= _max 

def validate_entry_part2(entry):
    rule, password = [i.strip() for i in entry.split(':')]
    _range, char = rule.split(' ')
    _min, _max = [int(i) - 1 for i in _range.split('-')]
    a = _min < len(password) and password[_min] == char
    b = _max < len(password) and password[_max] == char
    return (a or b) and not (a and b)

def part1(l):
    return len(filter(validate_entry_part1, l))

def part2(l):
    return len(filter(validate_entry_part2, l))

if __name__ == '__main__':
    l = sys.stdin.readlines()
    print part1(l)
    print part2(l)

