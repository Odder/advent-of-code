from algas.input import lines, tokens
from algas.aoc.aoc import part1, part2, part1and2, part1and2yield
from collections import deque


@part1and2yield()
def solve():
    bricks = []
    grid = [[[0 for _ in range(400)] for __ in range(10)] for ___ in range(10)]
    ls = list(lines())
    support_map = [set() for _ in range(len(ls) + 1)]
    supported_map = [set() for _ in range(len(ls) + 1)]

    for line in lines():
        a, b = line.split('~')
        a = tuple(int(x) for x in a.split(','))[::-1]
        b = tuple(int(x) for x in b.split(','))[::-1]
        bricks.append((a, b))

    for i, brick in enumerate(sorted(bricks)):
        (az, ay, ax), (bz, by, bx) = sorted(brick)
        touching = set()
        while az > -1 and len(touching) == 0:
            for x in range(ax, bx + 1):
                if grid[x][ay][az]:
                    touching |= {grid[x][ay][az]}
            for y in range(ay, by + 1):
                if grid[ax][y][az]:
                    touching |= {grid[ax][y][az]}

            if len(touching) > 0:
                for c in touching:
                    support_map[c] |= {i+1}
                    supported_map[i+1] |= {c}
                break
            az -= 1
            bz -= 1

        for x in range(min(ax, bx), max(ax, bx) + 1):
            grid[x][ay][az+1] = i+1
        for y in range(min(ay, by), max(ay, by) + 1):
            grid[ax][y][az+1] = i+1
        for z in range(min(az, bz), max(az, bz) + 1):
            grid[ax][ay][z+1] = i+1

    remove_set = set()
    fragile_set = set()
    total = 0
    for i in range(1, len(bricks) + 1):
        if len(support_map[i]) == 0:
            remove_set |= {i}
        for c in supported_map[i]:
            if all(len(supported_map[n]) > 1 for n in support_map[c]):
                remove_set |= {c}
            else:
                fragile_set |= {c}
        else:
            fragile_set |= {i}

    yield len(remove_set)

    for i in fragile_set:
        falling_bricks = {i}
        q = deque(support_map[i])
        while q:
            j = q.pop()
            if not (supported_map[j] - falling_bricks):
                falling_bricks |= {j}
                for k in support_map[j]:
                    q.append(k)
        total += len(falling_bricks) - 1
    yield total


if __name__ == '__main__':
    pass
