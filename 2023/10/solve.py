from algas.input import lines
from algas.spaces.s2 import neighbours, directions_side, diagonals
from algas.aoc.aoc import part1and2
from algas.search import DFS
from collections import deque


@part1and2()
def solve1():
    grid = []
    original_grid = []
    start = (0, 0)
    mapping = {
        '.': [],
        '-': [(0, -1), (0, 1)],
        '|': [(-1, 0), (1, 0)],
        'L': [(-1, 0), (0, 1)],
        'J': [(-1, 0), (0, -1)],
        'F': [(1, 0), (0, 1)],
        '7': [(1, 0), (0, -1)],
        'S': directions_side,
    }
    # Create edges
    for i, line in enumerate(lines()):
        row = []
        for j, c in enumerate(line):
            row.append(mapping[c])
            if c == 'S':
                start = (i, j)
        grid.append(row)
        original_grid.append(list(line))

    # DFS + path (path is memory intense... sorry)
    seen = {}
    longest = 2
    path_grid = [[0 for _ in range(len(grid[i]))] for i in range(len(grid))]
    for q, (i, j), depth, path in DFS((start, 0, [start])):
        if (i, j) in seen:
            continue
        seen[(i, j)] = min(depth, seen.get((i, j), 999999999))
        for n in neighbours(grid, (i, j), grid[i][j]):
            q.append((n, depth + 1, path + [n]))

            if n == start and (depth + 1) // 2 > longest:
                path_grid = [[0 for _ in range(len(grid[row]))] for row in range(len(grid))]
                for p_i, p_j in path:
                    path_grid[p_i][p_j] = 1
                longest = (depth + 1) // 2

    # Rotate 45 deg and do a ray casting alg approach
    inside = 0
    for diag in diagonals(grid):
        is_inside = 0
        for i, j, _ in diag:
            inside += int(is_inside and path_grid[i][j] == 0)
            if path_grid[i][j] == 1 and original_grid[i][j] not in 'FJ':
                is_inside = not is_inside

    return longest, inside


if __name__ == '__main__':
    pass
