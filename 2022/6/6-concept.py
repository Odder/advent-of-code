import sys
sys.path.append('C:/Users/oscar/Code/Bnanan/Python/algas/src')
from algas.input import lines
from aoc.aoc import part1, part2


@part2(14)
@part1(4)
def main(n):
    line = next(lines())
    for i in range(n, len(line)):
        if len(set(line[i-n:i])) == n:
            return i
