from algas.input import tokens_filter
from algas.aoc.aoc import part1, part2
import math
from functools import reduce


def lcm(a, b):
    return a*b // math.gcd(a, b)


def lcm_many(*args):
    return reduce(lambda r, a: lcm(r, a), args, 1)


@part2(lambda nw: [x for x in nw if x[-1] == 'A'], 0)
@part1(lambda nw: ['AAA'], 0)
def solve2(start, n):
    lines = [list(x) for x in tokens_filter(regex=r'[A-Z]+')]
    dirs = ['LR'.index(x) for x in lines[0][0]]
    network = {node: [l, r] for node, l, r in lines[2:]}

    currs = start(network)
    seen = [{} for x in network if x[-1] == 'A']
    cycles = [0] * len(currs)
    while any(curr[-1] != 'Z' for curr in currs):
        for i, curr in enumerate(currs):
            currs[i] = network[curr][dirs[n % len(dirs)]]
            if currs[i][-1] == 'Z':
                if currs[i] in seen[i] and cycles[i] == 0 and (n - seen[i][currs[i]]) % len(dirs) == 0:
                    cycles[i] = n - seen[i][currs[i]]

                seen[i][currs[i]] = n
                if all(cycles):
                    return lcm_many(*cycles)
        n += 1
    return n


if __name__ == '__main__':
    pass
