from algas.input import lines
from algas.spaces.s2 import neighbours, directions_side, indices
from algas.aoc.aoc import part1, part2, part1and2
from algas.search import PFS, BFS
from collections import defaultdict
import re
import math


@part1(42)
def solve1(n):
    grid = [list(line) for line in lines()]
    start = indices(grid, 'S')[0]
    end = indices(grid, 'E')[0]
    grid[start[0]][start[1]] = 'a'
    grid[end[0]][end[1]] = 'z'

    dists = defaultdict(int)

    for q, dist, node in PFS((0, start)):
        if node == end:
            return dists[end]

        for neigh in neighbours(grid, node, directions_side):
            if ord(grid[node[0]][node[1]]) + 1 >= ord(grid[neigh[0]][neigh[1]]):
                new_dist = dists[node] + 1

                if neigh not in dists or new_dist < dists[neigh]:
                    dists[neigh] = new_dist
                    q.append((new_dist, neigh))


@part2(42)
def solve2(n):
    grid = [list(line) for line in lines()]
    start = indices(grid, 'S')[0]
    end = indices(grid, 'E')[0]
    grid[start[0]][start[1]] = 'a'
    grid[end[0]][end[1]] = 'z'

    dists = defaultdict(int)

    for q, dist, node in PFS((0, end)):
        if grid[node[0]][node[1]] == 'a':
            return dists[node]

        for neigh in neighbours(grid, node, directions_side):
            if ord(grid[node[0]][node[1]]) - 1 <= ord(grid[neigh[0]][neigh[1]]):
                new_dist = dists[node] + 1

                if neigh not in dists or new_dist < dists[neigh]:
                    dists[neigh] = new_dist
                    q.append((new_dist, neigh))


@part1(42)
def solve1(n):
    grid = [list(line) for line in lines()]
    start = indices(grid, 'S')[0]
    end = indices(grid, 'E')[0]
    grid[start[0]][start[1]] = 'a'
    grid[end[0]][end[1]] = 'z'

    seen = set()

    for q, dist, node in BFS((0, start)):
        if node == end:
            return dist

        for neigh in neighbours(grid, node, directions_side):
            if ord(grid[node[0]][node[1]]) + 1 >= ord(grid[neigh[0]][neigh[1]]):
                if neigh not in seen:
                    seen |= {neigh}
                    q.append((dist + 1, neigh))


@part2(42)
def solve2(n):
    grid = [list(line) for line in lines()]
    start = indices(grid, 'S')[0]
    end = indices(grid, 'E')[0]
    grid[start[0]][start[1]] = 'a'
    grid[end[0]][end[1]] = 'z'

    seen = set()

    for q, dist, node in BFS((0, end)):
        if grid[node[0]][node[1]] == 'a':
            return dist

        for neigh in neighbours(grid, node, directions_side):
            if ord(grid[node[0]][node[1]]) - 1 <= ord(grid[neigh[0]][neigh[1]]):
                if neigh not in seen:
                    seen |= {neigh}
                    q.append((dist + 1, neigh))


# @part1and2(42)
def solve2(n):
    # logic goes here
    return 42


if __name__ == '__main__':
    pass
