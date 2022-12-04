def main():
    contained = 0
    overlaps = 0
    with open('input', 'r') as f:
        for line in f:
            l1, u1, l2, u2 = (int(x) for x in line.strip().replace('-', ',').split(','))
            if (l1 <= l2 and u1 >= u2) or (l1 >= l2 and u1 <= u2):
                contained += 1
            if (l1 <= l2 <= u1) or (l1 <= u2 <= u1) or (l2 <= l1 <= u2) or (l2 <= u1 <= u2):
                overlaps += 1

    return contained, overlaps


if __name__ == '__main__':
    part1, part2 = main()
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')
