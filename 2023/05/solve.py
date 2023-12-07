from algas.input import lines
from algas.lists import group
from algas.aoc.aoc import part1, part2
from algas.ranges import Range, simplify
from itertools import batched


@part2(lambda seeds: [Range(a, a+b) for a, b in batched(seeds, n=2)])
@part1(lambda seeds: [Range(seed, seed) for seed in seeds])
def solve2(parse_seeds):
    groups = list(group(lines(), ''))
    seeds = sorted(parse_seeds([int(x) for x in groups[0][0].split(' ')[1:]]))

    for purpose in groups[1:]:
        ranges = sorted([(Range(s, s+r - 1), d - s) for d, s, r in (map(int, line.split(' ')) for line in purpose[1:])])
        i, j, c, dist = 0, 0, seeds[0].left, []
        while i < len(seeds):
            c = max(c, seeds[i].left)
            if j >= len(ranges):
                right = seeds[i].right
                dist.append(Range(c, right))
                i += 1
                continue
            if seeds[i].left > ranges[j][0].right:
                j += 1
                continue
            if c < ranges[j][0].left:
                right = min(ranges[j][0].left, seeds[i].right)
                dist.append(Range(c, right))
            else:
                right = min(ranges[j][0].right, seeds[i].right)
                dist.append(Range(c + ranges[j][1], right + ranges[j][1]))

            c = right + 1
            i += int(c > seeds[i].right)
            j += int(j < len(ranges) and ranges[j][0].right < c)

        seeds = list(simplify(sorted(dist)))
    return min([x.left for x in seeds])


if __name__ == '__main__':
    pass
