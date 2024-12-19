from collections import defaultdict
from algs.spaces.imaginary_s2 import load_grid, floodfill
from aoc.input import lines, grouped_lines, tokens_pattern, nums
from aoc.aoc import part1, part2, part1and2, part1and2yield
from algs.search import BFS


@part1()
def solve1(its=100):
    bots = []
    for line in lines():
        px, py, vx, vy = nums(line)
        bots.append(((px, py), (vx, vy)))

    bound_x = 101
    bound_y = 103
    quads = [0, 0, 0, 0]

    its = 0
    while True:
        its += 1
        grid = [[' ']*103 for _ in range(107)]
        igrid = defaultdict(float)
        for (px, py), (vx, vy) in bots:
            x, y = px + vx * its, py + vy * its
            while x < 0:
                x += bound_x
            while y < 0:
                y += bound_y
            x %= bound_x
            y %= bound_y
            grid[x][y] = '#'
            igrid[x+y*1j] = 1
            if x < bound_x // 2 and y < bound_y // 2:
                quads[0] += 1
            if x < bound_x // 2 and y > bound_y // 2:
                quads[1] += 1
            if x > bound_x // 2 and y < bound_y // 2:
                quads[2] += 1
            if x > bound_x // 2 and y > bound_y // 2:
                quads[3] += 1

        if len(floodfill(igrid)) < 350:
            print(f'---------- {its} -----------')
            for row in grid:
                print(''.join(row))

    return quads[0] * quads[1] * quads[2] * quads[3]

if __name__ == '__main__':
    pass
