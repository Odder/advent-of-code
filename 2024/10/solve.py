from algs.spaces.imaginary_s2 import load_grid, directions_side
from aoc.input import lines
from aoc.aoc import part1and2
from algs.search import BFS


@part1and2()
def solve():
    grid = load_grid(lines(), int)
    starts = [k for k in grid.keys() if not grid[k]]
    total = 0
    for start in starts:
        trail_set = set()
        trail_list = []
        for q, pos, depth in BFS((start, 1)):
            if depth > 9:
                trail_set.add(pos)
                trail_list.append(pos)
            for off in directions_side:
                if grid[pos+off] == depth:
                    q.append((pos+off, depth+1))
        total += len(trail_set) + len(trail_list)*1j

    return int(total.real), int(total.imag)

if __name__ == '__main__':
    pass
