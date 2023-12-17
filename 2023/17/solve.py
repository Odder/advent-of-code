from algas.input import lines
from algas.spaces.s2 import directions_side, in_bounds
from algas.search import PFS
from algas.aoc.aoc import part1, part2
from collections import defaultdict


@part2(4, 10)
@part1(0, 3)
def solve(lower, upper):
    grid = [[int(x) for x in line] for line in lines()]
    start = (0, 0)
    end = (len(grid)-1, len(grid[0])-1)
    dists = defaultdict(int)

    for q, dist, (x, y), prev in PFS((0, start, (-1, -1))):
        if (x, y) == end:
            return dist
        for direction in directions_side:
            if direction == prev or direction == (-prev[0], -prev[1]):
                continue
            heat_loss = 0
            for i in range(1, upper + 1):
                ox = x + direction[0]*i
                oy = y + direction[1]*i
                if not in_bounds(grid, ox, oy):
                    break
                heat_loss += grid[ox][oy]
                state = (ox, oy, prev)
                if i >= lower and (state not in dists or dist + heat_loss < dists[state]):
                    dists[state] = dist + heat_loss
                    q.append((dist + heat_loss, (ox, oy), direction))
    return -1


if __name__ == '__main__':
    pass
