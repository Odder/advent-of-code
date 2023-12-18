from algas.input import tokens
from algas.aoc.aoc import part1, part2
from itertools import pairwise


def area(points):  # shoelace
    return abs(sum((x1*y2 - y1*x2 for (x1, y1), (x2, y2) in pairwise(points))) // 2)


@part2(True, [1j, 1, -1j, -1])
@part1(False, {'U': -1, 'R': 1j, 'D': 1, 'L': -1j})
def solve2(use_hex, dirs):
    moves = [(d, int(l), c) for d, l, c in tokens()]
    pos = 0
    walls = 0
    vertices = []
    for direction, length, colour in moves:
        if use_hex:
            length = int(colour[2:7], 16)
            direction = int(colour[7], 16)
        walls += length
        pos = pos + length*dirs[direction]
        vertices.append(pos)
    return area((w.real, w.imag) for w in vertices) + walls//2 + 1


if __name__ == '__main__':
    pass
