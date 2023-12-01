import sys
sys.path.append('C:/Users/oscar/Code/Bnanan/Python/algas/src')
from algas.input import tokens_filter
from algas.spaces.s2 import rays, directions, traverse
from aoc.aoc import part1and2


@part1and2()
def main():
    grid = [list(row) for row in tokens_filter(int, '\d')]
    visible = 0
    best = 0

    for i, j, cell in traverse(grid):
        "Part 1"
        for ray in rays(grid, (i, j), directions):
            if len(ray) < 1 or max(ray) < cell:
                visible += 1
                break

        "Part 2"
        scenic = 1
        for ray in rays(grid, (i, j), directions):
            dist = 0
            for dist, tree in enumerate(ray):
                if tree >= cell:
                    break
            scenic *= dist + 1
        best = max(scenic, best)

    return visible, best
