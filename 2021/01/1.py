import sys
sys.path.append('C:/Users/oscar/Code/Bnanan/Python/algas/src')
from algas.lists import top_n, group
from algas.input import ints, lines
from aoc.aoc import part1, part2


@part2(3)
@part1(1)
def main(n):
    k = 0
    prev = 10**10
    measures = list(ints())
    for i in range(len(measures)-n + 1):
        k += 1 if sum(measures[i:i+n]) > prev else 0
        prev = sum(measures[i:i+n])

    return k
