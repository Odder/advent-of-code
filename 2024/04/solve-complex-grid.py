from algs.spaces.imaginary_s2 import load_grid, directions_all
from aoc.input import lines
from aoc.aoc import part1and2

@part1and2()
def solve1():
    grid = load_grid(lines())
    p1, p2 = 0, 0
    for pos in list(grid.keys()):
        for dir in directions_all:
            if grid[pos] == 'X' and grid[pos + dir] == 'M' and grid[pos + 2*dir] == 'A' and grid[pos + 3*dir] == 'S':
                p1 += 1

        for rot in (1, 1j, -1, -1j):
            if grid[pos] == 'A' and grid[pos + rot*(-1-1j)] == 'M' and grid[pos + rot*(-1+1j)] == 'M' and grid[pos + rot*(+1-1j)] == 'S' and grid[pos + rot*(+1+1j)] == 'S':
                p2 += 1
    return p1, p2

if __name__ == '__main__':
    pass
