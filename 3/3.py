def part1():
    total = 0
    with open('input', 'r') as f:
        for line in f:
            size = len(line)//2
            char = (set(line[:size]) & set(line[size:])).pop()
            total += score(char)

    return total


def part2():
    total = 0
    with open('input', 'r') as f:
        for line in f:
            char = (set(line.strip()) & set(f.readline()) & set(f.readline())).pop()
            total += score(char)

    return total


def score(char):
    c = ord(char)
    return c - 38 if c < 95 else c - 96


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
