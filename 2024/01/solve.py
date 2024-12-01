from collections import defaultdict
from aoc.input import tokens_pattern
from aoc.aoc import part1and2yield


@part1and2yield()
def solve1():
    pile_a = []
    pile_b = []
    pile_b_counts = defaultdict(int)
    for a, b in tokens_pattern(r'(\d+)\s+(\d+)'):
        pile_a.append(int(a))
        pile_b.append(int(b))
        pile_b_counts[int(b)] += 1
    yield sum(abs(a-b) for a, b in zip(sorted(pile_a), sorted(pile_b)))
    yield sum(pile_b_counts[a] * a for a in pile_a)

if __name__ == '__main__':
    pass
