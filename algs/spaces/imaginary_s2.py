import math
from collections import defaultdict

directions_side = [1, 1j, -1, -1j]
directions_diag = [-1-1j,-1+1j, 1-1j, 1+1j]
directions_all = directions_side + directions_diag

def load_grid(data, data_type=str):
    grid = defaultdict(data_type)
    for x, row in enumerate(data):
        for y, cell in enumerate(row):
            grid[x+y*1j] = data_type(cell)
    return grid

def cells(grid, start, direction, length):
    return [grid[start + direction*step] for step in range(length)]


def neighbours(grid, coord, dirs):
    boundary = len(grid) + len(grid[0])*1j
    for direction in dirs:
        neigh = coord + direction
        if 0 <= neigh.real < boundary.real and 0 <= neigh.imag < boundary.imag:
            yield tuple(neigh)


def indices(grid, needle):
    return [k for k in grid if grid[k] == needle]


def gp(grid):
    print('------Grid------')
    for row in grid:
        print(row)

def floodfill(grid):
    seen = set()
    regions = []
    keys = list(grid.keys())
    for p in keys:
        if p in seen:
            continue
        region = []
        q = [p]
        while q:
            pos = q.pop()
            if pos in seen:
                continue
            seen.add(pos)
            region.append(pos)
            for d in directions_side:
                if grid[pos] == grid[pos + d]:
                    q.append(pos + d)
        regions.append(region)
    return regions

def perimeter(grid):
    perimeter = 0
    for cell in grid:
        added = 4
        for d in directions_side:
            if cell + d in grid:
                added -= 1
        perimeter += added
    return perimeter

def sides(grid):
    sides = 0
    walls = set()
    for cell in grid:
        for d in directions_side:
            if not cell + d in grid:
                walls.add(cell + d/4)

    seen = set()
    for wall in walls:
        if wall in seen:
            continue
        seen.add(wall)
        k = 1
        dirs = [1,-1] if wall.real % 1 == 0 else [1j,-1j]
        for d in dirs:
            while wall+k*d in walls:
                seen.add(wall+k*d)
                k += 1
            sides += 1
    return sides


if __name__ == '__main__':
    g = [[1, 2, 3], [3, 5, 6], [7, 8, 9]]
    gp(g)

