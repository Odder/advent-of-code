from algas.input import lines
from algas.aoc.aoc import part1, part2
from algas.spaces.s2 import traverse
from bisect import bisect_left as bs
from itertools import combinations


@part2(1000000)
@part1(2)
def solve1(expansion):
    grid = [list(line) for line in lines()]
    void_rows = [i for i, line in enumerate(grid) if '#' not in line]
    void_cols = [j for j, line in enumerate(zip(*grid)) if '#' not in line]
    galaxies = [(i, j) for i, j, cell in traverse(grid) if cell == '#']
    dist = 0
    voids = 0

    for (i, j), (k, l) in combinations(galaxies, 2):
        voids += abs(bs(void_rows, i) - bs(void_rows, k)) + abs(bs(void_cols, j) - bs(void_cols, l))
        dist += abs(i-k) + abs(j-l)

    return dist + voids * (expansion-1)


if __name__ == '__main__':
    pass
