from algas.aoc.aoc import part1, part2
import math


@part2([(61677571, 430103613071150)])
@part1([(61, 430), (67, 1036), (75, 1307), (71, 1150)])
def solve1(races):
    return math.prod([abs(math.ceil((t + math.sqrt(t ** 2 - 4 * d)) / 2) - math.floor((t - math.sqrt(t ** 2 - 4 * d)) / 2)) - 1 for t, d in races])


if __name__ == '__main__':
    pass
