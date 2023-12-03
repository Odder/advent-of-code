from algas.input import lines
from algas.spaces.s2 import traverse, neighbours
from algas.aoc.aoc import part1, part2


def neighs(grid, x, x_end, y):
    return grid[max(0, y-1)][max(0, x-1):min(len(grid[0]), x_end+1)] \
         + grid[min(len(grid)-1, y+1)][max(0, x-1):min(len(grid[0]), x_end+1)] \
         + [grid[y][x-1] if x - 1 > 0 else '.'] \
         + [grid[y][x_end] if x_end < len(grid[0]) else '.']


@part1(42)
def solve1(n):
    grid = [list(row) for row in lines()]
    nums = []
    for y, line in enumerate(grid):
        x = 0
        while x < len(line):
            x_end = x
            while x_end < len(grid[0]) and grid[y][x_end].isdigit():
                x_end += 1

            if x_end > x:
                for neigh in neighs(grid, x, x_end, y):
                    if not (neigh.isdigit() or neigh == '.'):
                        nums.append(int(''.join(grid[y][x:x_end])))

            x = x_end + 1
    print( len(nums), len(set(nums)))
    return sum(nums)


@part2(42)
def solve2(n):
    grid = [list(row) for row in lines()]
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    gears = []

    def expand_to_num(line, x):
        x_start = x
        x_end = x + 1
        while x_start >= 0 and line[x_start].isdigit():
            x_start -= 1
        while x_end < len(line) and line[x_end].isdigit():
            x_end += 1
        return int(''.join(line[x_start+1:x_end]))

    for i, j, c in traverse(grid):
        if c == '*':
            neigh_nums = set()
            for neigh_i, neigh_j in neighbours(grid, (i, j), dirs):
                neigh_c = grid[neigh_i][neigh_j]
                if neigh_c.isdigit():
                    neigh_nums |= {expand_to_num(grid[neigh_i], neigh_j)}
            if len(neigh_nums) == 2:
                a, b = neigh_nums
                gears.append(a * b)

    return sum(gears)


if __name__ == '__main__':
    pass
