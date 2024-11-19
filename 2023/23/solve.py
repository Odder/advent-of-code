from algas.input import lines, tokens
from algas.spaces.s2 import neighbours, directions_side, indices, in_bounds, rotate
from algas.misc import Cyclic
from algas.search import BFS, DFS
from algas.aoc.aoc import part1, part2, part1and2
from functools import cache
from itertools import permutations
from collections import Counter, defaultdict, deque
import re
import math


# @part1()
def solve1():
    grid = [list(x) for x in lines()]
    start = 1j
    end = (len(grid)-1) + (len(grid)-2)*1j
    highest = 0
    for q, pos, path in BFS((start, {start})):
        if pos == end:
            print('route found!')
            highest = max(highest, len(path))
        for offset in (-1, 1, 1j, -1j):
            neigh = pos + offset
            if neigh.real < 0 or neigh.imag < 0 or neigh.real >= len(grid) or neigh.imag >= len(grid[0]):
                continue
            c = grid[int(neigh.real)][int(neigh.imag)]
            if neigh in path or c == '#':
                continue
            if c == '>' and offset == -1j or c == '<' and offset == 1j or c == '^' and offset == 1 or c == 'v' and offset == -1:
                continue
            q.append((neigh, path | {neigh}))

    return highest-1


@part2(42)
def solve2(n):
    grid = [list(x) for x in lines()]
    start = 1j
    end = (len(grid)-1) + (len(grid)-1)*1j
    edges = []
    seen = set()
    letters = list(''.join(x) for x in permutations('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 2))
    assigned = {start: 'AA', end: 'ZZ'}
    corners = {start, end}
    for q, pos, prev, s, length in DFS((start, -1j, start, 0)):
        if pos in seen:
            # print('already seen!', pos, s)
            continue

        seen |= {pos}
        neighs = []
        for offset in (-1, 1, 1j, -1j):
            neigh = pos + offset
            if neigh == prev or neigh.real < 0 or neigh.imag < 0 or neigh.real >= len(grid) or neigh.imag >= len(grid[0]):
                continue
            if neigh in corners and length > 1:
                edges.append((*sorted([assigned[s], assigned[neigh]]), length + 1))
            c = grid[int(neigh.real)][int(neigh.imag)]
            if c == '#':
                continue
            neighs.append(neigh)

        if len(neighs) > 1:
            corners |= {pos}
            assigned[pos] = letters[len(assigned)-2]
            edges.append((*sorted([assigned[s], assigned[pos]]), length))
            for neigh in neighs:
                q.append((neigh, pos, pos, 1))
        elif neighs:
            q.append((neighs[0], pos, s, length+1))
        else:
            print('Dead end found', s)

    for edge in sorted(edges):
        print(list(edge))

    mapping = defaultdict(list)
    for v1, v2, length in sorted(edges):
        mapping[v1].append((v2, length))
        mapping[v2].append((v1, length))

    print(mapping)

    while True:
        seen = set()
        total = 0
        pos = 'AA'
        print('----------------')
        while True:
            print('---', pos, total)
            options = [x for x in mapping[pos] if x[0] not in seen]
            if not options:
                total = 10*10-1
                print('no options')
                break
            for i, (neigh, length) in enumerate(options):
                print(f'{i+1} - {neigh} ({length})')
            pick = int(input('> '))
            total += options[pick-1][1]
            seen |= {pos}
            pos = options[pick-1][0]
            if pos == 'ZZ':
                print('the end')
                break
        print(f'Total score: {total-1}')
    return 42

# @part2(42)
# def solve2(n):
#     grid = [list(x) for x in lines()]
#     start = 1j
#     end = (len(grid)-1) + (len(grid)-2)*1j
#     dists = {}
#     paths = defaultdict(set)
#     for q, pos, path in BFS((0, start, {start})):
#         if pos == end:
#             print('route found!')
#             return len(paths[pos])
#         neighs = 0
#         for offset in (-1, 1, 1j, -1j):
#             neigh = pos + offset
#             if neigh.real < 0 or neigh.imag < 0 or neigh.real >= len(grid) or neigh.imag >= len(grid[0]):
#                 continue
#             c = grid[int(neigh.real)][int(neigh.imag)]
#             if neigh in path or c == '#':
#                 continue
#             neighs += 1
#             q.append((neigh, path | {neigh}))
#         if neighs > 0:
#             print(pos, neigh)
#
#     return highest-1


# @part1and2(42)
def solve2(n):
    # logic goes here
    return 42


if __name__ == '__main__':
    pass
