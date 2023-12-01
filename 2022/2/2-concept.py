import sys
sys.path.append('C:/Users/oscar/Code/Bnanan/Python/algas/src')
from algas.input import lines
from aoc.aoc import part1, part2


@part2({'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7})
@part1({'A X': 4, 'A Y': 8, 'A Z': 3, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 7, 'C Y': 2, 'C Z': 6})
def main(outcomes):
    return sum(outcomes[line] for line in lines())
