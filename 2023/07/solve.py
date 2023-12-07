from algas.input import tokens
from algas.aoc.aoc import part1, part2
from collections import Counter


@part2('J23456789TQKA')
@part1('23456789TJQKA')
def solve(ranks):
    def score(hand):
        if ranks[0] == 'J' and 'J' in hand:
            return max(score(hand.replace('J', x)) for x in ranks[1:])
        return sorted(Counter(hand).values())[::-1]

    hands = ((score(hand), *map(ranks.index, hand), int(bet)) for hand, bet in tokens())
    return sum(i*bet for i, (*_, bet) in enumerate(sorted(hands), 1))


if __name__ == '__main__':
    pass
