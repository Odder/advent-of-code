from algs.maths import crt
from aoc.input import lines
from aoc.aoc import part1, part2


@part1()
def solve1():
    [start, table] = lines()
    start = int(start)
    buses = [int(x) for x in table.split(',') if x != 'x']

    ans = 0
    best = 10**10

    for bus in buses:
        curr = bus + (start // bus) * bus
        if curr < best:
            print('new leader', bus, curr)
            best = curr
            ans = (curr - start) * bus
    return ans

@part2()
def solve2():
    [_, table] = lines()
    buses = [int(x) if x != 'x' else 0 for x in table.split(',')]

    cgrs = []

    for i, bus in enumerate(buses):
        if bus == 0:
            continue
        remainder = (bus + (bus - (i % bus))) % bus
        cgrs.append((remainder, bus))

    return crt(cgrs)[0]

if __name__ == '__main__':
    pass
