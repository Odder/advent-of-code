import re
from aoc.input import lines
from aoc.aoc import part1and2

@part1and2()
def solve():
    passport = {}
    present = 0
    valid = 0
    validators = {
        'byr': lambda x: 1920 <= int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) <= 2020,
        'eyr': lambda x: 2020 <= int(x) <= 2030,
        'hgt': lambda x: 59 <= int(x[:-2]) <= 76 if x[-2:] == 'in' else 150 <= int(x[:-2]) <= 193 if x[-2:] == 'cm' else False,
        'hcl': lambda x: re.match(r'^#[0-9a-f]{6}$', x),
        'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda x: re.match(r'^[0-9]{9}$', x),
    }
    for line in lines():
        if line == '':
            if all(r in passport for r in validators.keys()):
                present += 1
                if all(validators[key](passport[key]) for key in passport):
                    valid += 1
            passport = {}
            continue
        for attr in line.split(' '):
            key, value = attr.split(':')
            if key == 'cid':
                continue
            passport[key] = value
    return present, valid

if __name__ == '__main__':
    pass
