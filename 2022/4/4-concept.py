import sys
sys.path.append('C:/Users/oscar/Code/Bnanan/Python/algas/src')
from algas.input import tokens_filter
from algas.ranges import Range
from aoc.aoc import part1, part2


@part2(lambda r1, r2: bool(r1 & r2))
@part1(lambda r1, r2: r1 in r2)
def main(scorer):
    entries = ((Range(l1, u1), Range(l2, u2)) for l1, u1, l2, u2 in tokens_filter(int, '\d+'))
    return sum(int(scorer(l, r)) for l, r in entries)
