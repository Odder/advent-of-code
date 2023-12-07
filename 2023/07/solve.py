from algas.input import lines, tokens
from algas.aoc.aoc import part1, part2, part1and2
from collections import Counter


@part2(True, 'J23456789TQKA', [])
@part1(False, '23456789TJQKA', [])
def solve(flag, ranks, hands):
    def score(hand):
        if flag and 'J' in hand:
            return max(score(hand.replace('J', x, 1)) for x in ranks if x != 'J')
        return list(sorted(Counter(hand).values(), reverse=True))

    for hand, bet in tokens(str):
        hands.append((score(hand) + [ranks.index(x) for x in hand], bet))

    return sum((i+1)*int(bet) for i, (_, bet) in enumerate(sorted(hands)))


if __name__ == '__main__':
    pass
