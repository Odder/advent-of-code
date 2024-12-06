from aoc.input import lines
from aoc.aoc import part1, part2

@part1()
def solve1():
    grid = [[c for c in line] for line in lines()]
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if i < len(grid) and j+3 < len(grid[i]):
                if grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i][j+3] in ['XMAS', 'SAMX']:
                    total += 1
            if i+3 < len(grid) and j < len(grid[i]):
                if grid[i][j] + grid[i+1][j] + grid[i+2][j] + grid[i+3][j] in ['XMAS', 'SAMX']:
                    total += 1
            if i+3 < len(grid) and j+3 < len(grid[i]):
                if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] + grid[i+3][j+3] in ['XMAS', 'SAMX']:
                    total += 1
            if i+3 < len(grid) and j-3 > -1:
                if grid[i][j] + grid[i+1][j-1] + grid[i+2][j-2] + grid[i+3][j-3] in ['XMAS', 'SAMX']:
                    total += 1
    return total

@part2()
def solve2():
    grid = [[c for c in line] for line in lines()]
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if i+2 < len(grid) and j+2 < len(grid[i]):
                if grid[i+1][j+1] == 'A' and grid[i][j] + grid[i][j+2] + grid[i+2][j+2] + grid[i+2][j] in ['MMSS', 'SMMS', 'SSMM', 'MSSM']:
                    total += 1
    return total

if __name__ == '__main__':
    pass
