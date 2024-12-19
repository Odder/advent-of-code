from algs.spaces.imaginary_s2 import load_grid
from aoc.input import lines, nums
from aoc.aoc import part1and2yield
from algs.search import BFS

def solve(grid):
    seen = set()
    k = 1
    for q, pos, dist in BFS((0, 0)):
        k+=1
        if pos in seen:
            continue
        if pos == 70 + 70j:
            return dist
        seen.add(pos)
        for d in [1, 1j, -1, -1j]:
            if grid[pos + d] != '.' or pos + d in seen:
                continue
            q.append((pos + d, dist + 1))
    return False

def create_grid(k):
    grid = load_grid([['.' for _ in range(71)] for __ in range(71)], str)
    for x, y in [nums(line) for line in list(lines())[:k]]:
        c = x + y*1j
        grid[c] = '#'
    return grid

def coord_to_pos(coord):
    x, y = nums(coord)
    return x + y*1j

@part1and2yield()
def solve():
    yield solve(create_grid(1024))

    low, high = 1024, 3451
    while low < high:
        mid = (low + high) // 2
        if solve(create_grid(mid)):
            low = mid + 1
        else:
            high = mid
    yield list(lines())[low-1]

if __name__ == '__main__':
    pass
