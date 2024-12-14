from algs.spaces.imaginary_s2 import load_grid, floodfill, perimeter, sides
from aoc.input import lines
from aoc.aoc import part1and2yield


@part1and2yield()
def solve1():
    grid = load_grid(lines())
    regions = floodfill(grid)
    yield sum(len(region)*perimeter(region) for region in regions)
    yield sum(len(region)*sides(region) for region in regions)

if __name__ == '__main__':
    pass
