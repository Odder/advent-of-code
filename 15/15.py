from collections import defaultdict
from re import findall


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def read():
    lines = []
    with open('input', 'r') as file:
        for line in file:
            lines.append([int(x) for x in findall('[\-0-9]+', line)])
    return lines


def scan(lines, loi):
    loi_ranges = []
    for x1, y1, x2, y2 in lines:
        sensor = (x1, y1)
        beacon = (x2, y2)
        dist = manhattan(sensor, beacon)
        width = dist - abs(y1 - loi)
        if width >= 0:
            loi_ranges.append((x1 - width, x1 + width))
    loi_ranges.sort()
    return loi_ranges


def part1():
    ranges = scan(read(), 2_000_000)

    total = 0
    left = ranges[0][0]
    for l, r in ranges:
        total += r - max(left, l) if r > left else 0
        left = max(r, left)
    return total


def part2():
    loi = 2_000_000
    lines = read()

    for i in range(0, loi*2):
        ranges = scan(lines, i)
        total = 0
        left = ranges[0][0]
        if i % 100_000 == 0:
            print(f'scanned {i} lines')
        for l, r in ranges:
            if l > left + 1:
                print(f'x: {l-1}, y: {i}, score: {(l-1)*4_000_000+i}')
            total += r - max(left, l) if r > left else 0
            left = max(r, left)
            if left > loi*2:
                break
    return total


if __name__ == '__main__':
    print(f'Part 1:', part1())
    print(f'Part 2:', part2())
