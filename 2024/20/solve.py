from collections import defaultdict as dd
from algs.spaces.imaginary_s2 import load_grid, indices, directions_side
from aoc.input import lines
from aoc.aoc import part1, part2
from algs.search import BFS

@part1()
def solve1(ans=0):
    grid = load_grid(lines())
    s = indices(grid, 'S')[0]
    e = indices(grid, 'E')[0]
    opt = 0
    seen = set()
    best_path = []
    for q, pos, depth, path in BFS((s, 0, [s])):
        if pos == e:
            opt = depth
            best_path = path
            break

        if pos in seen:
            continue
        seen.add(pos)
        for d in directions_side:
            npos = pos + d
            if grid[npos] != '#':
                q.append((npos, depth + 1, path+[npos]))
    dists = dd(lambda: 10**9)
    seen = set()
    for q, pos, depth, path in BFS((e, 0, [e])):
        if pos in seen:
            continue

        seen.add(pos)
        dists[pos] = depth
        if pos == s:
            break

        for d in directions_side:
            npos = pos + d
            if npos in seen:
                continue
            if grid[npos] != '#':
                q.append((npos, depth + 1, path+[npos]))
    for depth, p in enumerate(best_path):
        seen = set()
        for a in directions_side:
            for b in directions_side:
                if a + b in seen:
                    continue
                seen.add(a + b)
                npos = p + a + b
                if grid[npos] != '#' and dists[npos] + depth + 2 <= opt - 100:
                    ans += 1
                    break
    return ans


@part2()
def solve2(ans=0):
    grid = load_grid(lines())
    s = indices(grid, 'S')[0]
    e = indices(grid, 'E')[0]
    opt = 0
    seen = set()
    best_path = []
    for q, pos, depth, path in BFS((s, 0, [s])):
        if pos == e:
            opt = depth
            best_path = path
            break

        if pos in seen:
            continue
        seen.add(pos)
        for d in directions_side:
            npos = pos + d
            if grid[npos] != '#':
                q.append((npos, depth + 1, path+[npos]))
    dists = dd(lambda: 10**9)
    seen = set()
    for q, pos, depth, path in BFS((e, 0, [e])):
        if pos in seen:
            continue

        seen.add(pos)
        dists[pos] = depth
        if pos == s:
            break

        for d in directions_side:
            npos = pos + d
            if grid[npos] != '#':
                q.append((npos, depth + 1, path+[npos]))

    for i, p in enumerate(best_path):
        seen = set()
        for q, pos, depth in BFS((p, 0)):
            if depth > 20:
                break
            if pos in seen:
                continue
            seen.add(pos)

            if grid[pos] != '#' and i + depth + dists[pos] <= opt - 100:
                ans += 1

            for d in directions_side:
                npos = pos + d
                if not npos in seen:
                    q.append((npos, depth + 1))
    return ans

if __name__ == '__main__':
    pass
