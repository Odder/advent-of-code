from itertools import pairwise
from aoc.input import ints
from aoc.aoc import part1, part2


@part1()
def solve1():
    ones = 0
    threes = 1
    for prev, curr in pairwise([0] + sorted(ints())):
        match curr-prev:
            case 1:
                ones += 1
            case 3:
                threes += 1
    return ones * threes


@part2()
def solve2():
    numbers = [0] + sorted(ints())
    dp = [0] * len(numbers)
    dp[0] = 1

    for i in range(1, len(numbers)):
        for j in range(i - 1, -1, -1):
            if numbers[i] - numbers[j] <= 3:
                dp[i] += dp[j]
            else:
                break
    return dp[-1]

if __name__ == '__main__':
    pass
