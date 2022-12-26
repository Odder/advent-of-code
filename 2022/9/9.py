from collections import defaultdict

directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'R': (0, 1),
    'L': (0, -1)
}


def read():
    with open('input', 'r') as file:
        return [line.strip().split() for line in file]


def main(n=1):
    visited = defaultdict(bool)
    rope = [[0, 0] for _ in range(n+1)]
    visited[tuple(rope[0])] = True
    for move, dist in read():
        os_x, os_y = directions[move]
        for _ in range(int(dist)):  # Applying 1 step at a time
            rope[0] = [rope[0][0] + os_x, rope[0][1] + os_y]
            for i in range(1, len(rope)):  # Moving 1 knot at a time
                head, tail = rope[i-1], rope[i]
                if abs(head[0] - tail[0]) < 2 and abs(head[1] - tail[1]) < 2:  # skip if neighbour
                    continue

                for k in (0, 1):
                    if abs(head[k] - tail[k]) > 0:
                        tail[k] += 1 if head[k] > tail[k] else -1
            visited[tuple(rope[-1])] = True

    return sum([int(x) for x in visited.values()])


if __name__ == '__main__':
    print(f'Part 1: {main()}')
    print(f'Part 2: {main(9)}')
