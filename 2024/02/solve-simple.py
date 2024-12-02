from itertools import pairwise, combinations
from aoc.input import tokens
from aoc.aoc import part1and2

def safe(points):
    inc, dec, diffs = zip(*[(a < b, a > b, abs(a-b) <= 3) for a, b in pairwise(points)])
    return (all(inc) or all(dec)) and all(diffs)

@part1and2()
def solve():
    lines = list(tokens(modifier=int))
    near_lines = [combinations(line, len(line)-1) for line in lines]
    return sum(map(safe, lines)), sum(map(lambda near: any(map(safe, near)), near_lines))

if __name__ == '__main__':
    pass
