from collections import defaultdict as dd
from algs.spaces.imaginary_s2 import load_grid, indices, directions_side
from aoc.input import lines
from aoc.aoc import part1, part2
from algs.search import BFS

@part2(20)
@part1(2)
def solve1(ps=2, ans=0):
    grid = load_grid(lines())
    s = indices(grid, 'S')[0]
    e = indices(grid, 'E')[0]
    best_path = []
    dists = dd(lambda: 1000000)
    seen = set()

    for q, pos, depth, path in BFS((e, 0, [e])):
        seen.add(pos)
        dists[pos] = depth
        if pos == s:
            best_path = path[::-1]
            break

        for d in directions_side:
            npos = pos + d
            if npos in seen:
                continue
            if grid[npos] != '#':
                q.append((npos, depth + 1, path+[npos]))

    for depth, p in enumerate(best_path):
        for a in range(-ps,ps+1):
            for b in range(-(ps-abs(a)), (ps+1)-abs(a)):
                npos = p + a + b*1j
                if dists[p] - (dists[npos] + abs(a) + abs(b)) >= 100:
                    ans += 1
    return ans

if __name__ == '__main__':
    pass
