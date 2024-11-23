from aoc.input import ints
from aoc.aoc import part1, part2, part1and2

def solve(x, lines):
    seen = set()
    for line in lines:
        if x - line in seen:
            return line * (x - line)
        seen.add(line)
    return 0

@part1()
def solve1():
    return solve(2020, ints())

@part2()
def solve2():
    lines = list(ints())

    for line in lines:
        if x := solve(2020-line, lines):
            return x * line

if __name__ == '__main__':
    pass
