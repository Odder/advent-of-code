import sys
sys.path.append('C:/Users/oscar/Code/Bnanan/Python/algas/src')
from algas.input import tokens_split
from aoc.aoc import part1, part2
from collections import defaultdict


@part2(lambda fs: min(f for f in fs.values() if (fs['/'] - f) <= 40_000_000))
@part1(lambda fs: sum(f for f in fs.values() if f < 100_000))
def main(scorer):
    path = []
    folders = defaultdict(int)
    for line in tokens_split():
        match list(line):
            case ['$', 'cd', '..']:
                path.pop()
            case ['$', _, folder]:
                path.append(folder)
            case [size, _] if size.isnumeric():
                for i in range(len(path)):
                    folders['/'.join(path[:i+1])] += int(size)

    for folder in folders:
        print(f'{folder}: {folders[folder]}')

    return scorer(folders)
