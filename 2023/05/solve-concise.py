from algas.input import lines
from algas.lists import group
from algas.aoc.aoc import part1, part2
from algas.ranges import Range
from itertools import batched


@part2(lambda seeds: [Range(a, a+b) for a, b in batched(seeds, n=2)])
@part1(lambda seeds: [Range(seed, seed) for seed in seeds])
def solve2(parse_seeds):
    groups = list(group(lines(), ''))
    seeds = parse_seeds([int(x) for x in groups[0][0].split(' ')[1:]])

    for purpose in groups[1:]:
        ranges = ([(Range(s, s+r), d - s) for d, s, r in (map(int, line.split(' ')) for line in purpose[1:])])
        new = []
        while len(seeds) > 0:
            seed = seeds.pop()
            for r, offset in ranges:
                if intersection := (seed & r):
                    new.append(intersection + offset)
                    new.extend(seed ^ r)
                    break
            else:
                new.append(seed)
        seeds = new
    return min(seeds).left


if __name__ == '__main__':
    pass
