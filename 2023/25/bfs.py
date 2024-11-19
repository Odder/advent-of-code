from algas.aoc.aoc import part1
from algas.search import DFS, BFS
from itertools import pairwise
from collections import defaultdict
import random


def bfs(edges, a, b):
    came_from = [{a: None}, {b: None}]
    for q, n, direction in BFS([(a, 0), (b, 1)]):
        for m in edges[n]:
            if m in came_from[(direction + 1) % 2]:
                if direction:
                    path = []
                    curr = m if direction else n
                    while curr:
                        path.append(curr)
                        curr = came_from[0][curr]
                    path = path[::-1]
                    curr = n if direction else m
                    while curr:
                        path.append(curr)
                        curr = came_from[1][curr]
                    return path

            if m in came_from[direction]:
                continue

            q.append((m, direction))
            came_from[direction][m] = n


@part1()
def solve():
    nodes = set()
    edges = defaultdict(list)
    with open('input', 'r') as f:
        for line in f:
            source, dests = line.strip().split(': ')
            nodes.add(source)
            for dest in dests.split(' '):
                nodes.add(dest)
                edges[source].append(dest)
                edges[dest].append(source)
    seen = set()

    left_iter = iter(set(nodes))

    while True:
        for _ in range(7):
            a, b = next(left_iter), next(left_iter)
            path = bfs(edges, a, b)
            for edge in pairwise(path):
                seen.add(tuple(sorted(edge)))

        left = set(nodes)
        for q, n in DFS((random.choice(list(nodes)),)):
            for m in edges[n]:
                if (n, m) in seen or (m, n) in seen:
                    continue
                if m in left:
                    q.append((m, ))
                    left.remove(m)

        if len(left) > 100:
            return len(left) * (len(nodes) - len(left))


if __name__ == '__main__':
    pass
