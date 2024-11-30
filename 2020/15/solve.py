from aoc.aoc import part1, part2

@part2(30_000_000)
@part1(2020)
def solve1(limit):
    seed = [13,16,0,12,15,1]
    last_seen = {n: (-1, i) for i, n in enumerate(seed)}
    last = seed[-1]
    for i in range(len(seed), limit):
        a, b = last_seen[last]
        last = b - a if a != -1 else 0
        last_seen[last] = (last_seen[last][1], i) if last in last_seen else (-1, i)
    return last

if __name__ == '__main__':
    pass
