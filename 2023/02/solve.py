from algas.input import tokens_filter
from algas.aoc.aoc import part1and2


@part1and2(0, 0)
def solve(t, p):
    limits = {'green': 13, 'blue': 14, 'red': 12}       # Part 1
    for i, game in enumerate(tokens_filter(modifier=tuple, regex=r'(\d+) (red|green|blue)')):
        maxes = {'green': 0, 'blue': 0, 'red': 0}       # Part 2
        for x, colour in game:
            maxes[colour] = max(maxes[colour], int(x))  # Part 2
            if int(x) > limits[colour]:                 # Part 1
                i = -1                                  # Part 1
        t += i + 1                                      # Part 1
        p += maxes['red'] * maxes['green'] * maxes['blue']  # Part 2
    return t, p


if __name__ == '__main__':
    pass
