from algas.input import lines, tokens
from algas.spaces.s2 import neighbours, directions_side, indices, in_bounds, rotate, gp
from algas.search import BFS, DFS
from algas.aoc.aoc import part1, part2, part1and2


@part1(64)
def solve1(n):
    grid = [list(x) for x in lines()]
    s = indices(grid, 'S')[0]
    grid[s[0]][s[1]] = '.'
    even = set()
    odd = set()
    seen = set()
    for q, (x, y), depth in BFS((s, 0)):
        if depth == n:
            break
        for neigh in neighbours(grid, (x, y), directions_side):
            if neigh not in seen and grid[neigh[0]][neigh[1]] == '.':
                seen |= {neigh}
                if (depth % 2) == 0:
                    even |= {neigh}
                else:
                    odd |= {neigh}
                q.append((neigh, depth+1))
    return len(odd)


@part2(26501365)
def solve2(n):
    grid = [list(x) for x in lines()]
    s = indices(grid, 'S')[0]
    grid[s[0]][s[1]] = '.'
    a = []
    for i in range(len(grid) // 2, len(grid)*3, len(grid)):
        seen = set()
        counts = [0, 0]
        k = 0
        for q, (x, y), depth in BFS((s, 0)):
            k += 1
            if depth == i:
                break
            for ox, oy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                neigh = ((x + ox), (y + oy))

                if neigh not in seen and grid[neigh[0] % len(grid)][neigh[1] % len(grid[0])] == '.':
                    seen |= {neigh}
                    counts[(depth + 1) % 2] += 1
                    q.append((neigh, depth+1))
        a.append(counts[i % 2])
        # print(i, counts)

    def f(x, a0, a1, a2):
        b0 = a0
        b1 = a1 - a0
        b2 = a2 - a1
        return b0 + b1 * x + (x * (x - 1) // 2) * (b2 - b1)

    return f(n // len(grid), *a)


if __name__ == '__main__':
    pass
