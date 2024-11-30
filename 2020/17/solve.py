from collections import defaultdict, deque
from itertools import product

from aoc.input import ints, lines, grouped_lines, tokens_filter, tokens_pattern
from aoc.aoc import part1, part2, part1and2, part1and2yield

def neighs_3(x, y, z):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                if i == x and j == y and k == z:
                    continue
                yield i, j, k


def neighs_4(x, y, z, w):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                for l in range(w-1, w+2):
                    if i == x and j == y and k == z and l == w:
                        continue
                    yield i, j, k, l

def neighs(point):
    for diff in product([-1, 0, 1], repeat=len(point)):
        if not any(diff):
            continue
        yield tuple(p+d for p, d in zip(point, diff))

@part2(True)
@part1(False)
def solve1(four_dimensional):
    active = set()
    for x, line in enumerate(lines()):
        for y, char in enumerate(line):
            if char == '#':
                if four_dimensional:
                    active.add((x, y, 0, 0))
                else:
                    active.add((x, y, 0))

    for _ in range(6):
        next_active = set()
        to_check = set()
        for cube in active:
            active_neighs = 0
            for neigh in neighs(cube):
                if neigh in active:
                    active_neighs += 1
                else:
                    to_check.add(neigh)
            if active_neighs == 2 or active_neighs == 3:
                next_active.add(cube)
        for cube in to_check:
            active_neighs = 0
            for neigh in neighs(cube):
                if neigh in active:
                    active_neighs += 1
            if active_neighs == 3:
                next_active.add(cube)

        active = next_active

    return len(active)


if __name__ == '__main__':
    pass
