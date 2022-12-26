def main(n=3):
    points = 0
    with open('input', 'r') as f:
        for line in f:
            him, you = line.rstrip('\n').split(' ')
            him_ord = ord(him) - 65
            you_ord = ord(you) - 88

            points += points_by_outcome(him_ord, you_ord) if n == 2 else points_by_play(him_ord, you_ord)

    return points


def points_by_play(him, you):
    outcome = (you + 3 + 1 - him) % 3
    return you + 1 + outcome * 3


def points_by_outcome(him, you):
    play = (him + 2 + you) % 3
    return play + 1 + you * 3


if __name__ == '__main__':
    print(f'Part 1: {main(1)}')
    print(f'Part 2: {main(2)}')
