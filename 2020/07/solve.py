from collections import defaultdict, deque

from aoc.input import tokens_pattern
from aoc.aoc import part1and2yield


@part1and2yield()
def solve():
    src = defaultdict(set)
    dest = {}

    for line in tokens_pattern(r'(.+) bags contain ((\d+) (.+?) bags?(, |.))?((\d+) (.+?) bags?(, |.))?((\d+) (.+?) bags?(, |.))?((\d+) (.+?) bags?(, |.))?'):
        origin = line[0]
        numbers = [int(x) if x else 0 for x in line[2::4] if x]
        contains = [x for x in line[3::4] if x]
        dest[origin] = list(zip(numbers, contains))
        for bag in contains:
            src[bag] |= {origin}

    seen = set()
    q = ['shiny gold']
    while q:
        bag = q.pop()
        if bag in seen:
            continue
        seen |= {bag}
        for a in src[bag]:
            print(a)
            q.append(a)

    yield len(seen) - 1

    total = 0
    q = deque([(1, 'shiny gold')])
    while q:
        k, bag = q.popleft()
        total += k
        for c, b in list(dest[bag]):
            q.append((c*k, b))

    yield total - 1

if __name__ == '__main__':
    pass
