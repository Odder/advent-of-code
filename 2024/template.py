from collections import deque
from collections import defaultdict as dd

from algs.spaces.imaginary_s2 import load_grid, indices
from algs.lists import lmap, cnt
from aoc.input import ints, lines, grouped_lines, tokens_filter, tokens_pattern, nums
from aoc.aoc import part1, part2, part1and2, part1and2yield
from algs.search import BFS, DFS, PFS


@part1()
def solve1(ans=0):

    return ans


@part2()
def solve2():
    return 0


@part1and2()
def solve():
    return 0, 0


@part1and2yield()
def solve4():
    yield 0
    yield 0


def examples():
    for line in lines():
        pass

    for group in grouped_lines():
        for line in group:
            pass

    [towels], patterns = grouped_lines(lambda x: x.split(', '))

    for key, value in tokens_pattern(regex=r'(\d+): (.+)'):
        pass

    grid = load_grid(lines(), int)

    for q, pos, depth in BFS((2, 0)):
        pass

    for q, score, pos, depth in PFS((0, (2, 0))):
        q.append(score, (pos, depth))
        pass

if __name__ == '__main__':
    pass
