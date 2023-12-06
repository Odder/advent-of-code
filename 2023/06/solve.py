from algas.aoc.aoc import part1, part2
import math


@part2([(61677571, 430103613071150)], 1)
@part1([(61, 430), (67, 1036), (75, 1307), (71, 1150)], 1)
def solve1(races, res):
    for t, d in races:
        if (disc := t ** 2 - 4 * d) < 0:
            continue
        x1 = math.ceil((t + math.sqrt(disc)) / 2)
        x2 = math.floor((t - math.sqrt(disc)) / 2)
        res *= abs(x2 - x1) - 1

    return res


if __name__ == '__main__':
    pass
