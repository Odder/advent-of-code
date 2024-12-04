import re
from aoc.input import lines
from aoc.aoc import part1, part2

@part1()
def solve1():
    total = 0
    for line in lines():
        total += sum(int(a)*int(b) for a, b in re.findall(r'mul\((\d+),(\d+)\)', line))
    return total

@part2()
def solve2():
    total = 0
    enabled = True
    for line in lines():
        for cmd, a, b in re.findall(r'(do\(\)|don\'t\(\)|mul\((\d+),(\d+)\))', line):
            match cmd:
                case 'do()':
                    enabled = True
                case 'don\'t()':
                    enabled = False
                case _ if enabled:
                    total += int(a) * int(b)
    return total

if __name__ == '__main__':
    pass
