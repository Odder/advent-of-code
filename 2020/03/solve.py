from algs.maths import prod
from aoc.input import lines
from aoc.aoc import part1, part2


@part2([(1,1), (1,3), (1,5), (1,7), (2,1)])
@part1([(1,3)])
def solve1(runs):
    def calc(offset):
        oi, oj = offset
        grid = list(list(line) for line in lines())
        trees = 0
        j = 0
        for i in range(0, len(grid), oi):
            trees += int(grid[i][j] == '#')
            j = (j + oj) % len(grid[0])

        return trees

    return prod(map(calc, runs))

if __name__ == '__main__':
    pass
