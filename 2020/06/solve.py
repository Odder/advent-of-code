from aoc.input import grouped_lines
from aoc.aoc import part1, part2

@part2(lambda x, y: x & y)
@part1(lambda x, y: x | y)
def solve1(op):
    ans = 0
    for group in grouped_lines():
        yes = set(group[0])
        for line in group[1:]:
            yes = op(yes, set(line))
        ans += len(yes)
    return ans

if __name__ == '__main__':
    pass
