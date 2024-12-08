from collections import defaultdict
from itertools import permutations
from algs.spaces.imaginary_s2 import load_grid
from aoc.input import lines
from aoc.aoc import part1, part2

@part2(0,100)
@part1(1,2)
def solve1(*args):
    grid = load_grid(lines())
    groups = defaultdict(list)
    for pos, cell in grid.items():
        if cell != '.':
            groups[cell].append(pos)

    anti = set()
    for pairs in groups:
        for a, b in permutations(groups[pairs], 2):
            for k in range(*args):
                if not b+(k*(b-a)) in grid:
                    break
                anti.add(b+(k*(b-a)))
    return len(anti)

if __name__ == '__main__':
    pass
