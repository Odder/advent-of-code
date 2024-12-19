from functools import cache
from algs.lists import lmap, cnt
from aoc.input import grouped_lines
from aoc.aoc import part1and2yield


@part1and2yield()
def solve1():
    [towels], patterns = grouped_lines(lambda x: x.split(', '))

    @cache
    def dp(pattern):
        if not pattern:
            return 1
        res = 0
        for towel in towels:
            if pattern.startswith(towel):
                res += dp(pattern[len(towel):])
        return res

    combs = lmap(dp, patterns)
    yield cnt(combs)
    yield sum(combs)

if __name__ == '__main__':
    pass
