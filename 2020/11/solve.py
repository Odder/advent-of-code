from collections import defaultdict
from algs.spaces.s2 import traverse
from aoc.input import lines
from aoc.aoc import part1, part2



@part2(1000, 5, False)
@part1(1, 4, True)
def solve2(max_k, max_occ, override):
    grid = [list(row) for row in lines()]
    neigh_map = defaultdict(list)

    for i, j, cell in traverse(grid):
        if cell == 'L':
            for oi, oj in [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                k = 1
                while 0 <= i+k*oi < len(grid) and 0 <= j+k*oj < len(grid[0]) and k <= max_k:
                    if override or grid[i+k*oi][j+k*oj] == 'L':
                        neigh_map[(i, j)].append((i+k*oi, j+k*oj))
                        break
                    k += 1

    changes = 1
    while changes:
        changes = 0
        updated = [row[:] for row in grid]
        for i, j, cell in traverse(grid):
            occ = 0
            for ni, nj in neigh_map[(i, j)]:
                occ += int(grid[ni][nj] == '#')
            if cell == 'L' and occ == 0:
                updated[i][j] = '#'
                changes += 1
            if cell == '#' and occ >= max_occ:
                updated[i][j] = 'L'
                changes += 1
        grid = [row[:] for row in updated]
        if changes == 0:
            break
    return sum(row.count('#') for row in grid)

if __name__ == '__main__':
    pass
