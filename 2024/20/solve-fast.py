from algs.spaces.imaginary_s2 import load_grid, indices, directions_side
from aoc.input import lines
from aoc.aoc import part1, part2

def manh(a, b):
    return int(abs(a.real - b.real) + abs(a.imag - b.imag))

@part2(20)
@part1(2)
def solve1(ps=2, ans=0):
    grid = load_grid(lines())
    s = indices(grid, 'S')[0]
    e = indices(grid, 'E')[0]
    best_path = [s]
    pos = s
    prev = -4
    while pos != e:
        for d in directions_side:
            npos = pos + d
            if d == -prev or grid[npos] == '#':
                continue
            best_path.append(npos)
            prev = d
            pos = npos

    t = 100
    k = 0
    for i, p in enumerate(best_path):
        j = i + t
        while j < len(best_path):
            k += 1
            dist = manh(best_path[j], p)
            if dist <= ps and j - dist - i >= t:
                ans += 1
                j += 1
            else:
                j += dist - ps if dist - ps > 0 else 1
    return ans

if __name__ == '__main__':
    pass
