import sys
sys.path.append('C:/Users/oscar/Code/Bnanan/Python/algas/src')
from algas.lists.lists import top_n, group
from algas.input.file import ints
from aoc.aoc import part1, part2


@part2(3)
@part1(1)
def main(n):
    return sum(top_n(map(sum, group(ints())), n))
