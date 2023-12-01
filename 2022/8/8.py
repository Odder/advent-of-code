






def read_grid():
    with open('input', 'r') as file:
        grid = [[int(x) for x in line.strip()] for line in file]

    return grid


def part1():
    grid = read_grid()
    visible = [[False for _ in x] for x in grid]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for x, y in directions:
        i = len(grid) - 1 if x < 0 else 0
        j = len(grid[0]) - 1 if y < 0 else 0
        while 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            peak = -1
            while 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                visible[i][j] = visible[i][j] or grid[i][j] > peak
                peak = max(grid[i][j], peak)
                if grid[i][j] == 9:
                    break
                i += x
                j += y
            i = i + 1 if x == 0 else (len(grid) - 1 if x < 0 else 0)
            j = j + 1 if y == 0 else (len(grid[0]) - 1 if y < 0 else 0)

    visible_trees = 0
    for row in visible:
        for tree in row:
            visible_trees += int(tree)
    return visible_trees


def part2():
    grid = read_grid()
    best_score = -1
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[i])-1):
            scenic_score = 1
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                distance = 1
                while 0 <= i + distance*x < len(grid) and 0 <= j + distance*y < len(grid[0]):
                    if grid[i + distance*x][j + distance*y] >= grid[i][j]:
                        break
                    distance += 1
                else:
                    distance -= 1

                scenic_score *= distance
            best_score = max(best_score, scenic_score)

    return best_score


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
