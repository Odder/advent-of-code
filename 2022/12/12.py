import heapq
from collections import defaultdict

matrix = []


def read():
    global matrix
    start, goal = (0, 0), (0, 0)
    with open('input', 'r') as file:
        matrix = [[ord(x) for x in list(line.strip())] for line in file]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == ord('S'):
                    start = (i, j)
                    matrix[i][j] = ord('a')
                if matrix[i][j] == ord('E'):
                    goal = (i, j)
                    matrix[i][j] = ord('z')
    return start, goal


def neighbours(coord):
    i, j = coord
    neighs = []
    for i_dir, j_dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        i_os, j_os = i+i_dir, j+j_dir
        if -1 < i_os < len(matrix) and -1 < j_os < len(matrix[0]) and matrix[i_os][j_os] <= matrix[i][j] + 1:
            neighs.append((i_os, j_os))
    return neighs


def search(start, goal):
    q = [(0, start)]
    dist = defaultdict(int)
    cameFrom = defaultdict(int)
    dist[start] = 0
    cameFrom[start] = 0

    while q:
        _, cand = heapq.heappop(q)
        if cand == goal:
            return dist[goal]
        for neigh in neighbours(cand):
            new_dist = dist[cand] + 1

            if neigh not in dist or new_dist < dist[neigh]:
                dist[neigh] = new_dist
                heapq.heappush(q, (new_dist, neigh))
                cameFrom[neigh] = neigh


def part1():
    s, e = read()
    steps = search(s, e)
    return steps


def part2():
    best = 10**7
    _, e = read()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == ord('a'):
                steps = search((i, j), e)
                if steps and steps < best:
                    best = steps
    return best


if __name__ == '__main__':
    print(f'Part 1:', part1())
    print(f'Part 2:', part2())
