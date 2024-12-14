from collections import defaultdict, deque
from math import floor

from algs.spaces.imaginary_s2 import load_grid, directions_side
from aoc.input import ints, lines, grouped_lines, tokens_filter, tokens_pattern
from aoc.aoc import part1, part2, part1and2, part1and2yield
from algs.search import BFS, DFS, PFS


@part1and2yield()
def solve1():
    grid = load_grid(lines())
    seen = set()
    regions = []
    keys = list(grid.keys())
    k = 0
    for p in keys:
        if p in seen:
            continue
        region = []
        q = deque([p])
        k += 1
        while q:
            pos = q.pop()
            if pos in seen:
                continue
            seen.add(pos)
            region.append(pos)
            for d in directions_side:
                if pos+d in seen:
                    continue
                if grid[pos] == grid[pos+d]:
                    q.append(pos+d)
        regions.append(region)

    total = 0
    for region in regions:
        area = len(region)
        perimeter = 0
        for piece in region:
            added = 4
            for d in directions_side:
                if piece+d in region:
                    added -= 1
            perimeter += added
        total += area * perimeter
    yield total

    total = 0
    for region in regions:
        area = len(region)
        sides = 0
        walls = set()
        for piece in region:
            added = 4
            for d in directions_side:
                if piece+d in region:
                    added -= 1
                else:
                    walls.add(piece + d/4.3)

        seen = set()
        for wall in walls:
            if any([x == wall for x in seen]):
                continue
            seen.add(wall)
            k = 1
            d = 1 if wall.real % 1 == 0 else 1j
            while wall+k*d in walls:
                seen.add(wall+k*d)
                k+=1
            k=1
            while wall-k*d in walls:
                seen.add(wall-k*d)
                k+=1
            sides += 1
        total += area * sides
    yield total

if __name__ == '__main__':
    pass
