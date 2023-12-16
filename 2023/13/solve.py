from algas.input import lines
from algas.lists import group
from algas.spaces.vectors import V
from algas.aoc.aoc import part1and2


@part1and2(V((0, 0)))
def solve1(p):
    for puzzle in group(lines(), splitter=''):
        rows = list(puzzle)

        for multiplier, axis in [(100, rows), (1, list(zip(*rows)))]:
            for i in range(1, len(axis)):
                width = min(i, len(axis)-i)
                diffs = 0
                for k in range(width):
                    for a, b in zip(axis[i-k-1], axis[i+k]):
                        diffs += sum(a[j] != b[j] for j in range(len(a)))

                p += multiplier*i*V((diffs == 0, diffs == 1))

    return p


if __name__ == '__main__':
    pass
