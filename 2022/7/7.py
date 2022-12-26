from collections import defaultdict


def read_folders():
    with open('input', 'r') as f:
        path = []
        folders = defaultdict(int)
        for line in f:
            if line[:7] == '$ cd ..':
                path.pop()
            elif line[:5] == '$ cd ':
                path.append(line.strip()[5:])
            elif line[:3] in ('dir', '$ l'):
                continue
            else:
                size, _ = line.split()
                for i in range(len(path)):
                    folders['/'.join(path[:i+1])] += int(size)

    return folders


def part1():
    return sum(f for f in read_folders().values() if f < 100000)


def part2(limit=40_000_000):
    folders = read_folders()
    return min([f for f in folders.values() if (folders['/'] - f) <= limit])


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
