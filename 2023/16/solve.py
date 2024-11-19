from aoc.input import lines
from algs.spaces.s2 import in_bounds, traverse
from algs.search import BFS
from aoc.aoc import part1and2


def solve(grid, start):
    energised = [[0 for _ in range(len(line))] for line in grid]
    seen = set()
    for q, (x, y), (dir_x, dir_y) in BFS(start):
        if ((x, y), (dir_x, dir_y)) in seen:
            continue
        k = 1
        seen |= {((x, y), (dir_x, dir_y))}
        while in_bounds(grid, x + dir_x * k, y + dir_y * k):
            ox, oy = x + dir_x * k, y + dir_y * k
            energised[ox][oy] = 1
            match grid[ox][oy]:
                case '.':
                    k += 1
                    continue
                case '-':
                    q.append(((ox, oy), (0, -1)))
                    q.append(((ox, oy), (0, 1)))
                case '|':
                    q.append(((ox, oy), (-1, 0)))
                    q.append(((ox, oy), (1, 0)))
                case '/':
                    q.append(((ox, oy), (dir_y*-1, dir_x*-1)))
                case '\\':
                    q.append(((ox, oy), (dir_y*1, dir_x*1)))
            break
    return sum(x for _, _, x in traverse(energised))


@part1and2()
def solve1and2():
    grid = [list(line) for line in lines()]
    starts = [((i, -1), (0, 1)) for i in range(len(grid))]
    starts += [((i, len(grid[0])), (0, -1)) for i in range(len(grid))]
    starts += [((-1, i), (1, 0)) for i in range(len(grid[0]))]
    starts += [((len(grid), i), (-1, 0)) for i in range(len(grid[0]))]
    return solve(grid, ((0, -1), (0, 1))), max(solve(grid, start) for start in starts)


if __name__ == '__main__':
    pass
