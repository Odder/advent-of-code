import sys
sys.path.append('C:/Users/oscar/Code/Bnanan/Python/algas/src')
from algas.input import lines
from algas.lists import grouping, divide
from aoc.aoc import part1, part2


def score(char):
    c = ord(char)
    return c - 38 if c < 95 else c - 96


@part2(grouping(lines(), 3))
@part1(divide(x, 2) for x in lines())
def main(groups=None):
    return sum(score(set.intersection(*map(set, group)).pop()) for group in groups)
