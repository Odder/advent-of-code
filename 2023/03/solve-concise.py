from algas.input import lines
from algas.spaces.s2 import neighbours, directions_all
from algas.aoc.aoc import part1and2
import re
import math


@part1and2(0, set(), {})
def solve(gears, nums, num_map):
    grid = [list(row) for row in lines()]
    char_pos = [(i, num.start()) for i, line in enumerate(lines()) for num in re.finditer(r'[^\d.]', line)]

    for i, line in enumerate(lines()):
        for r_num in re.finditer(r'\d+', line):
            num_map.update({(i, j): ((i, r_num.start()), int(r_num.group())) for j in range(*r_num.span())})

    for i, j in char_pos:
        neigh_nums = {}
        for neigh in (x for x in neighbours(grid, (i, j), directions_all) if x in num_map):
            neigh_nums[num_map[neigh][0]] = num_map[neigh][1]
            nums |= {num_map[neigh]}

        if grid[i][j] == '*' and len(neigh_nums) == 2:
            gears += math.prod(neigh_nums.values())

    return sum(x[1] for x in list(nums)), gears


if __name__ == '__main__':
    pass