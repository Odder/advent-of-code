from collections import defaultdict
from itertools import pairwise

directions_side = [1, 1j, -1, -1j]
directions_diag = [-1-1j,-1+1j, 1-1j, 1+1j]
directions_all = directions_side + directions_diag

def load_grid(data, data_type=str):
    grid = defaultdict(data_type)
    for x, row in enumerate(data):
        for y, cell in enumerate(row):
            grid[x+y*1j] = data_type(cell)
    return grid

def traverse(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            yield i, j, cell

def cells(grid, start, direction, length):
    return [grid[start + direction*step] for step in range(length)]


def neighbours(grid, coord, dirs):
    boundary = len(grid) + len(grid[0])*1j
    for direction in dirs:
        neigh = coord + direction
        if 0 <= neigh.real < boundary.real and 0 <= neigh.imag < boundary.imag:
            yield tuple(neigh)


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

