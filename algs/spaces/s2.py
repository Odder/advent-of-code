from algs.spaces.vectors import V
from itertools import pairwise

directions_side = [(0, 1), (1, 0), (0, -1), (-1, 0)]
directions_diag = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
directions_all = directions_side + directions_diag


def rays(grid, coord, dirs):
    boundary_x, boundary_y = len(grid), len(grid[0])
    for direction in dirs:
        ray = []
        cell_x, cell_y = coord[0] + direction[0], coord[1] + direction[1],
        while 0 <= cell_x < boundary_x and 0 <= cell_y < boundary_y:
            ray.append(grid[cell_x][cell_y])
            cell_x += direction[0]
            cell_y += direction[1]

        yield ray


def in_bounds(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def diagonals(grid):
    rows, cols = len(grid), len(grid[0])
    diags = [[] for _ in range(rows + cols - 1)]

    for row in range(rows):
        for col in range(cols):
            diags[row + col].append((row, col, grid[row][col]))

    return diags


def traverse(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            yield i, j, cell


def neighbours(grid, coord, dirs):
    boundary = V((len(grid), len(grid[0])))
    for direction in dirs:
        neigh = V(coord) + V(direction)
        if V((0, 0)) <= neigh < boundary:
            yield tuple(neigh)


def to_map(grid):
    mapping = {}
    for i, j, cell in traverse(grid):
        if cell not in mapping:
            mapping[cell] = []
        mapping[cell].append((i, j))
    return mapping


def indices(grid, needle):
    return [(i, j) for i, j, cell in traverse(grid) if cell == needle]


def rotate(grid, times=1):
    match((times + 4) % 4):
        case 0:
            return grid
        case 1:
            return [list(reversed(row)) for row in zip(*grid)]
        case 2:
            return [row[::-1] for row in grid[::-1]]
        case 3:
            return [list(row) for row in reversed(list(zip(*grid)))]


def gp(grid):
    print('------Grid------')
    for row in grid:
        print(row)

def shoelace(points):
    return abs(sum((x1 * y2 - y1 * x2 for (x1, y1), (x2, y2) in pairwise(points))) // 2)


if __name__ == '__main__':
    g = [[1, 2, 3], [3, 5, 6], [7, 8, 9]]
    gp(g)
    gp(rotate(g))
    gp(rotate(g, 1))
    gp(rotate(g, 2))
    gp(rotate(g, 3))
    gp(rotate(g, -1))

