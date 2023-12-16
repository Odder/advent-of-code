from algas.input import lines
from algas.spaces.s2 import indices, in_bounds, rotate
from algas.misc import Cyclic
from algas.aoc.aoc import part1, part2


def tilt(grid):
    for i, j in indices(grid, 'O'):
        offset = 1
        while in_bounds(grid, i - offset, j) and grid[i - offset][j] == '.':
            offset += 1
        grid[i][j], grid[i - offset + 1][j] = grid[i - offset + 1][j], grid[i][j]


@part1()
def solve1():
    grid = [list(line) for line in lines()]
    tilt(grid)
    return sum(len(grid)-i for i, j in indices(grid, 'O'))


@part2()
def solve2():
    grid = [list(line) for line in lines()]

    for see, k in Cyclic(1_000_000_000):
        for _ in range(4):
            tilt(grid)
            grid = rotate(grid)
        see(str(grid))
    return sum(len(grid)-i for i, j in indices(grid, 'O'))


if __name__ == '__main__':
    pass
