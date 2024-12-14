
from algs.spaces.imaginary_s2 import load_grid
from aoc.input import lines, grouped_lines, tokens_pattern, nums
from aoc.aoc import part1, part2, part1and2, part1and2yield
from algs.search import BFS, DFS, PFS


@part1()
def solve1():
    costs = 0
    for group in grouped_lines():
        group = [x for x in group if x]
        a = nums(group[0])
        b = nums(group[1])
        target = nums(group[2])
        seen_a = dict()

        pos = [0, 0]
        i = 0
        while pos[0] < target[0] and pos[1] < target[1] and i <= 100:
            seen_a[tuple(pos)] = i
            pos = [pos[0] + a[0], pos[1] + a[1]]
            i+= 1

        pos = list(target)
        j = 0
        while pos[0] > -1 and pos[1] > -1 and j <= 100:
            if tuple(pos) in seen_a:
                costs += 3*seen_a[tuple(pos)] + j
            pos = [pos[0] - b[0], pos[1] - b[1]]
            j += 1
    return costs

@part2()
def solve2():
    costs = 0
    for group in grouped_lines():
        a = nums(group[0])
        b = nums(group[1])
        target = nums(group[2])
        target = [target[0] + 10000000000000, target[1] + 10000000000000]
        a_presses = (target[0] * b[1] - target[1] * b[0]) / (a[0] * b[1] - a[1] * b[0])
        b_presses = (target[1] * a[0] - target[0] * a[1]) / (a[0] * b[1] - a[1] * b[0])
        if b_presses == int(b_presses) and a_presses == int(a_presses):
            costs += 3*a_presses + b_presses
    return costs

if __name__ == '__main__':
    pass
