from collections import defaultdict, deque

from algs.ranges import Range, simplify
from algs.maths import prod
from aoc.input import ints, lines, grouped_lines, tokens_filter, tokens_pattern
from aoc.aoc import part1, part2, part1and2, part1and2yield


@part1and2yield()
def solve1():
    fields = {}
    all_ranges = []
    for field, min1, max1, min2, max2 in tokens_pattern(r'^([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)', file='input2'):
        r1 = Range(int(min1), int(max1))
        r2 = Range(int(min2), int(max2))
        fields[field] = r1, r2
        all_ranges.append(r1)
        all_ranges.append(r2)
    all_ranges.sort()
    all_ranges = list(simplify(all_ranges))[0]

    ans = 0
    valid_tickets = []
    for line in lines():
        for x in line.split(','):
            if not (int(x) in all_ranges):
                ans += int(x)
                break
        else:
            valid_tickets.append([int(x) for x in line.split(',')])
    yield ans

    col = 0
    field_names = [''] * len(fields.keys())
    fields_left = {x for x in fields.keys()}
    while fields_left:
        possible_fields = []
        for field in fields_left:
            [r1, r2] = fields[field]
            for ticket in valid_tickets:
                if ticket[col] not in r1 and ticket[col] not in r2:
                    break
            else:
                possible_fields.append(field)

        if len(possible_fields) == 1:
            field_names[col] = possible_fields[0]
            fields_left.remove(possible_fields[0])
        col = (col + 1) % len(fields)

    my_ticket = [int(i) for i in list(lines('input3'))[0].split(',')]
    yield prod(my_ticket[i] for i, field in enumerate(field_names) if field[:6] == 'depart')

if __name__ == '__main__':
    pass
