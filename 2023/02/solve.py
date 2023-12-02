from algas.input import tokens_filter
from algas.aoc.aoc import part1, part2


@part1(0)
def solve1(total):
    maxes = {'green': 13, 'blue': 14, 'red': 12}
    for i, game in enumerate(tokens_filter(modifier=tuple, regex=r'(\d+) (red|green|blue)')):
        for x, colour in game:
            if int(x) > maxes[colour]:
                i = -1
        total += i + 1
    return total


@part2(0)
def solve2(total):
    for game in tokens_filter(modifier=tuple, regex=r'(\d+) (red|green|blue)'):
        maxes = {'green': 0, 'blue': 0, 'red': 0}
        for x, colour in game:
            maxes[colour] = max(maxes[colour], int(x))
        total += maxes['red'] * maxes['green'] * maxes['blue']
    return total


if __name__ == '__main__':
    pass
