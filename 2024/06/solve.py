from algs.spaces.imaginary_s2 import load_grid
from aoc.input import lines
from aoc.aoc import part1and2yield


@part1and2yield()
def solve1():
    grid = load_grid(lines())
    dir = -1
    start_pos = 0
    for cell in grid:
        if grid[cell] == '^':
            start_pos = cell
            break

    pos = start_pos
    visited = set()
    visited.add(pos)
    while pos in grid and grid[pos]:
        if grid[pos + dir] == '#':
            dir *= -1j

        visited.add(pos)
        pos += dir
    yield len(visited)

    obstacles = 0
    for obstacle in visited:
        pos = start_pos
        dir = -1
        path_seen = set()
        while pos in grid and grid[pos]:
            if (pos, dir) in path_seen:
                obstacles += 1
                break
            path_seen.add((pos, dir))
            while grid[pos + dir] == '#' or pos + dir == obstacle:
                dir *= -1j
            pos += dir
    yield obstacles

if __name__ == '__main__':
    pass
