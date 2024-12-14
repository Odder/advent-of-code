from z3 import Ints, Solver, sat
from aoc.input import grouped_lines, nums
from aoc.aoc import part1, part2


@part2(10_000_000_000_000)
@part1(0)
def solve2(offset):
    costs = 0
    for group in grouped_lines():
        x1, y1, x2, y2, X, Y = nums(''.join(group))
        a, b = Ints('a b')

        solver = Solver()
        solver.add(x1 * a + x2 * b == X + offset, y1 * a + y2 * b == Y + offset)

        if solver.check() == sat:
            solution = solver.model()
            costs += 3*solution[a].as_long() + solution[b].as_long()
    return costs

if __name__ == '__main__':
    pass
