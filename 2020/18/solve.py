import re
from collections import defaultdict, deque
from algs.maths import shunting_yard
from aoc.input import ints, lines, grouped_lines, tokens_filter, tokens_pattern
from aoc.aoc import part1, part2, part1and2, part1and2yield


@part1()
def solve1():
    return sum(shunting_yard(expr, {'+': 1, '*': 1}) for expr in lines())


@part2()
def solve2():
    return sum(shunting_yard(expr, {'+': 2, '*': 1}) for expr in lines())

if __name__ == '__main__':
    pass
