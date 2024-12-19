from collections import defaultdict as dd
from aoc.input import grouped_lines
from aoc.aoc import part1and2

@part1and2(0, 0)
def solve1(p1, p2):
    groups = list(grouped_lines())
    towels = groups[0][0].split(', ')
    for pattern in groups[1]:
        dp = dd(int)
        dp[0] = 1
        for i in range(1, len(pattern)+1):
            for towel in towels:
                if pattern[i-len(towel):i] == towel:
                    dp[i] += dp[i-len(towel)]
        p1 += 1 if dp[len(pattern)] else 0
        p2 += dp[len(pattern)]

    return p1, p2

if __name__ == '__main__':
    pass
