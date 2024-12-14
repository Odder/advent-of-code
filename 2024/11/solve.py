from collections import defaultdict as dd
from aoc.input import tokens
from aoc.aoc import part1, part2

@part2(1000)
@part1(25)
def solve(its):
    stones = {stone: 1 for stone in tokens(int)[0]}
    for _ in range(its):
        new = dd(int)
        for num, stones in stones.items():
            match num:
                case _ if num == 0:
                    new[1] += stones
                case x if len(str(num)) % 2 == 0:
                    half = len(str(x)) // 2
                    new[int(str(x)[:half])] += stones
                    new[int(str(x)[half:])] += stones
                case x:
                    new[x*2024] += stones
        stones = new
    return sum(stones.values())

if __name__ == '__main__':
    pass
