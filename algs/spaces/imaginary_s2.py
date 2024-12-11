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


if __name__ == '__main__':
    g = [[1, 2, 3], [3, 5, 6], [7, 8, 9]]
    gp(g)

