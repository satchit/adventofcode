import re
import sys

def parse_input(text):
    passports = []
    passport = {}
    for line in text.splitlines():
        if not line.strip():
            passports.append(passport)
            passport = {}
        passport.update(dict(item.split(':') for item in line.split()))
    if passport:
        passports.append(passport)
    return passports

def validate_passports(passports, rules):
    valid = 0
    for passport in passports:
        for key in rules:
            if key not in passport or not rules[key](passport[key].strip()):
                break
        else:
            valid += 1
    return valid

def part1(passports):
    required_keys = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    rules = dict((k, lambda x: x.strip()) for k in required_keys)
    return validate_passports(passports, rules)
    

def part2(passports):

    def validate_hgt(x):
        a = re.search(r'^([0-9]+)([incm]{2}$)', x)
        if a:
            val, units = a.groups()
            if units == 'cm':
                return int(val) >= 150 and int(val) <= 193
            elif units == 'in':
                return int(val) >= 59 and int(val) <= 76


    rules = {
        'byr': lambda x: x.isdigit() and len(x) == 4 and int(x) >= 1920 and int(x) <= 2002,
        'iyr': lambda x: x.isdigit() and len(x) == 4 and int(x) >= 2010 and int(x) <= 2020, 
        'eyr': lambda x: x.isdigit() and len(x) == 4 and int(x) >= 2020 and int(x) <= 2030, 
        'hgt': validate_hgt,
        'hcl': lambda x: re.search(r'^#[0-9a-f]{6,6}$', x) is not None,
        'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'), 
        'pid': lambda x: x.isdigit() and len(x) == 9
    }

    return validate_passports(passports, rules)

if __name__ == '__main__':
    passports = parse_input(sys.stdin.read())
    print part1(passports)
    print part2(passports)

        