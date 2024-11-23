from aoc.input import lines
from aoc.aoc import part1and2


@part1and2()
def solve1():
    best = 0
    seats = [False] * 1000
    for line in lines():
        row_low = 0
        row_high = 127
        col_low = 0
        col_high = 7
        for char in line:
            match char:
                case 'F':
                    row_high -= (row_high - row_low + 1) // 2
                case 'B':
                    row_low += (row_high - row_low + 1) // 2
                case 'L':
                    col_high -= (col_high - col_low + 1) // 2
                case 'R':
                    col_low += (col_high - col_low + 1) // 2
        idx = row_low * 8 + col_low
        seats[idx] = True
        best = max(best, idx)

    return best, seats[100:950].index(False) + 100

if __name__ == '__main__':
    pass
