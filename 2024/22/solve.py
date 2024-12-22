from functools import cache
from itertools import pairwise
from algs.lists import nwise
from aoc.input import lines
from aoc.aoc import part1, part2
from collections import defaultdict as dd

@cache
def nxt(n):
    MASK_24 = (1 << 24) - 1
    n ^= (n << 6) & MASK_24
    n ^= (n >> 5)
    n ^= (n << 11) & MASK_24
    return n

@part1()
def solve1(ans=0):
    for secret in lines(mod=int):
        for _ in range(2000):
            secret = nxt(secret)
        ans += secret
    return ans

@part2()
def solve2():
    values = dd(lambda: dd(int))
    for secret in lines(mod=int):
        vals = [secret] + [secret := nxt(secret) for _ in range(2000)]
        for nums in nwise(vals, 5, rev=True):
            seq = (x % 10 for x in nums)
            pattern = tuple(b - a for a, b in pairwise(seq))
            values[pattern][secret] = nums[-1] % 10
    return max(sum(x.values()) for x in values.values())

if __name__ == '__main__':
    pass
