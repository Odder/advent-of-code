from algas.input import lines
from algas.aoc.aoc import part1, part2
from bisect import bisect_left


@part2(1000000)
@part1(2)
def solve1(expansion):
    grid = []
    expansion_rows = []
    expansion_cols = []
    for i, line in enumerate(lines()):
        grid.append(list(line))
        if '#' not in line:
            expansion_rows.append(i)

    for j in range(len(grid[0])):
        for row in grid:
            if row[j] == '#':
                break
        else:
            expansion_cols.append(j)

    dists = 0
    seen = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '#':
                for seen_i, seen_j in seen:
                    num_empty_rows = abs(bisect_left(expansion_rows, i) - bisect_left(expansion_rows, seen_i))
                    num_empty_cols = abs(bisect_left(expansion_cols, j) - bisect_left(expansion_cols, seen_j))
                    dists += abs(i-seen_i) + abs(j-seen_j) + (num_empty_rows + num_empty_cols) * (expansion-1)
                seen.append((i, j))

    return dists


if __name__ == '__main__':
    pass
