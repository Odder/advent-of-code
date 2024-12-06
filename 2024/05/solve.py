from collections import defaultdict, deque
from itertools import permutations
from aoc.input import ints, lines, grouped_lines, tokens_filter, tokens_pattern
from aoc.aoc import part1, part2, part1and2, part1and2yield

@part1()
def solve1():
    total = 0
    [rules, prints] = list(grouped_lines())
    after_map = defaultdict(set)
    for rule in rules:
        a, b = rule.split('|')
        after_map[int(a)].add(int(b))

    for prin in prints[1:]:
        prin = prin.split(',')
        seen = set()
        for page in prin:
            p = int(page)
            if after_map[p] & seen:
                break
            seen.add(p)
        else:
            total += int(prin[len(prin) // 2])

    return total


@part2()
def solve2():
    def order(ppp):
        ordered = []
        cp_ppp = [int(x) for x in ppp]
        while cp_ppp:
            for page in cp_ppp:
                p = int(page)
                cp_ppp.remove(page)
                ordered.append(p)

        return int(ordered[len(ordered) // 2])
    total = 0
    [rules, prints] = list(grouped_lines())
    after_map = defaultdict(set)
    before_map = defaultdict(set)
    for rule in rules:
        a, b = rule.split('|')
        after_map[int(a)].add(int(b))
        before_map[int(b)].add(int(a))

    for prin in prints[1:]:
        prin = prin.split(',')
        seen = set()
        for page in prin:
            p = int(page)
            if after_map[p] & seen:
                total += order(prin)
                break
            seen.add(p)
        else:
            continue

    return total

if __name__ == '__main__':
    pass
