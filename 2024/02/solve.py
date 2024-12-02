from itertools import pairwise

from aoc.input import tokens_split
from aoc.aoc import part1and2


def safe(L):
    direction = 1 if L[1] > L[0] else -1
    for a, b in pairwise(L):
        if abs(b - a) > 3:
            return False
        if (b - a) * direction < 1:
            return False
    return True

@part1and2()
def solve1():
    p1 = 0
    p2 = 0
    for line in tokens_split(modifier=int):
        dups = []
        for i in range(len(line)):
            cp = line[:]
            cp.pop(i)
            dups.append(cp)
        p1 += int(safe(line))
        p2 += int(any(safe(x) for x in dups))
    return p1, p2

if __name__ == '__main__':
    pass
