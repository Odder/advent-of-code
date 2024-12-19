from algs.spaces.imaginary_s2 import load_grid, indices
from aoc.input import lines
from aoc.aoc import part1and2yield
from algs.search import PFS

@part1and2yield()
def solve():
    grid = load_grid(lines())
    start = indices(grid, 'S')[0]
    end = indices(grid, 'E')[0]
    seen = dict()
    best_paths = []
    best_score = 10**10
    nodes = 0
    for q, score, (cell, d, path) in PFS((0, (start, 1j, [(0, 1j)]))):
        nodes += 1
        for dd, offset in [(1, 0), (1j, 1000), (-1j, 1000), (-1, 2000)]:
            if (cell, d*dd) in seen and seen[(cell, d*dd)] < score - offset:
                break
        else:
            if score > best_score:
                break
            if cell == end:
                best_score = score
                best_paths.append(path)
            seen[(cell, d)] = score
            k = 1 if score > 0 else 0
            while grid[cell + k*d] != '#':
                if cell + k*d == end:
                    q.append(score + k, (cell + k*d, d, path + [(k, d)]))
                if grid[cell + k*d + d*1j] != '#':
                    q.append(score + 1000 + k, (cell + k*d, d * 1j, path + [(k, d*1j)]))
                if grid[cell + k*d + d*-1j] != '#':
                    q.append(score + 1000 + k, (cell + k*d, d * -1j, path + [(k, d*-1j)]))
                k+=1
    yield best_score

    seen = set()
    grid[start] = 'O'
    for path in best_paths:
        cell = start
        d = 1j
        for steps, next_d in path:
            for _ in range(steps):
                cell += d
                seen.add(cell)
                grid[cell] = 'O'
            d = next_d
    yield len(indices(grid, 'O'))

if __name__ == '__main__':
    pass
