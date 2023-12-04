from algas.input import tokens_filter
from algas.aoc.aoc import part1and2


@part1and2([], [1 for _ in range(300)])
def solve2(scores, multipliers):
    for i, line in enumerate(tokens_filter(regex=r'\d+')):
        score = 0
        line_list = list(line)
        for _ in set(line_list[11:]) & set(line_list[1:11]):
            score += 1
            multipliers[i+score] += multipliers[i]
        scores.append((1 << score) >> 1)

    return sum(scores), sum(multipliers[:i+1])


if __name__ == '__main__':
    pass
