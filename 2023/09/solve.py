from algas.input import tokens
from algas.aoc.aoc import part1and2


@part1and2(0, 0)
def solve1(p1, p2):
    for seq in tokens(modifier=int):
        stack = [list(seq)]
        while any(stack[-1]):
            stack.append([b - a for a, b in zip(stack[-1][:-1], stack[-1][1:])])

        f, b = 0, 0
        for s in stack[::-1]:
            f, b = s[0] - f, s[-1] + b
        p1 += b
        p2 += f
    return p1, p2


if __name__ == '__main__':
    pass
