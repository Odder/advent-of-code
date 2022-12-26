from collections import deque, defaultdict


def read():
    grid = []
    storms = defaultdict(list)
    start, end = (0, 0), (0, 0)
    with open('input', 'r') as file:
        for i, line in enumerate(file):
            grid.append(list(line.strip()))
            for j, char in enumerate(line.strip()):
                if char in '><^v':
                    storms[(i, j)].append(char)

    for j, c in enumerate(grid[0]):
        if c == '.':
            start = (0, j)
    for j, c in enumerate(grid[-1]):
        if c == '.':
            end = (len(grid)-1, j)

    return (len(grid), len(grid[0])), storms, start, end


def stormy(grid, storms):
    max_i, max_j = grid
    new_storms = defaultdict(list)
    for cell in storms:
        while storms[cell]:
            storm = storms[cell].pop()
            if storm == '<':
                new_storms[cell[0], (((cell[1] - 2) % (max_j - 2)) + 1)].append(storm)
            if storm == '>':
                new_storms[cell[0], ((cell[1] % (max_j - 2)) + 1)].append(storm)
            if storm == '^':
                new_storms[((cell[0] - 2) % (max_i - 2)) + 1, cell[1]].append(storm)
            if storm == 'v':
                new_storms[(cell[0] % (max_i - 2)) + 1, cell[1]].append(storm)
    return new_storms


def solve(grid, storms, start, end, goals):
    q = deque([(start, 0, 0)])
    prev_depth = 0
    prev_goal = 0
    seen = {}
    while q:
        pos, depth, goal = q.popleft()
        i, j = pos
        if goal > prev_goal:
            prev_goal = goal
        if (pos, depth, goal) in seen:
            continue
        else:
            seen[(pos, depth, goal)] = True
        if prev_depth < depth:
            storms = stormy(grid, storms)
            prev_depth = depth
        if pos in storms:
            continue

        for new_i, new_j in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i, j)]:
            if (new_i, new_j) == goals[goal]:
                q.append(((new_i, new_j), depth + 1, goal + 1))
                if goal + 1 == len(goals):
                    return depth + 1
                continue
            elif new_i < 1 or new_j < 1 or new_i > (grid[0]-2) or new_j > (grid[1]-2):
                if (new_i, new_j) != start and (new_i, new_j) != end:
                    continue
            q.append(((new_i, new_j), depth + 1, goal))


def part1():
    grid, storms, start, end = read()
    return solve(grid, storms, start, end, [end])


def part2():
    grid, storms, start, end = read()
    return solve(grid, storms, start, end, [end, start, end])


if __name__ == '__main__':
    print(f'Part 1:', part1())
    print(f'Part 2:', part2())
