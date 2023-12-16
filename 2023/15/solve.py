from algas.input import lines, tokens
from algas.aoc.aoc import part1, part2, part1and2
from algas.spaces.s2 import traverse
from functools import reduce
from collections import OrderedDict
import re


def alg(txt):
    return reduce(lambda a, c: ((a + ord(c))*17) % 256, txt, 0)


@part1and2()
def solve():
    line = list(lines())[0]
    segments = line.split(',')
    boxes = [OrderedDict() for _ in range(256)]

    for i, segment in enumerate(segments):
        label, focal = re.split('[-=]', segment)
        box = boxes[alg(label)]
        if '=' in segment:
            box[label] = focal
        elif label in box:
            del box[label]

    return sum(alg(s) for s in segments), sum((i+1) * (j+1) * int(boxes[i][label]) for i, j, label in traverse(boxes))


if __name__ == '__main__':
    pass
