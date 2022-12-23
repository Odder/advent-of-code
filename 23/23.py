from collections import defaultdict
from itertools import product


class AdventuringElves:
    def __init__(self):
        self.elves = set()
        self.boundaries = (1000, 1000), (0, 0)
        self.moves = [
            (lambda i, j: {(i-1, j-1), (i-1, j), (i-1, j+1)}, lambda i, j: (i-1, j)),
            (lambda i, j: {(i+1, j-1), (i+1, j), (i+1, j+1)}, lambda i, j: (i+1, j)),
            (lambda i, j: {(i-1, j-1), (i, j-1), (i+1, j-1)}, lambda i, j: (i, j-1)),
            (lambda i, j: {(i-1, j+1), (i, j+1), (i+1, j+1)}, lambda i, j: (i, j+1)),
        ]

    def read(self):
        with open('input', 'r') as file:
            for i, line in enumerate(file):
                for j, char in enumerate(line.strip()):
                    if char == '#':
                        self.elves.add((i, j))

                        (min_i, min_j), (max_i, max_j) = self.boundaries
                        self.boundaries = (min(min_i, i), min(min_j, j)), (max(max_i, i), max(max_j, j))

    def round(self):
        targets = defaultdict(list)
        for i, j in list(self.elves):
            if not ((set(tuple(x) for x in product([i-1, i, i+1], [j-1, j, j+1])) - {(i, j)}) & self.elves):
                continue
            for neighs, target in self.moves:
                if self.elves & neighs(i, j):
                    continue
                targets[target(i, j)].append((i, j))
                break

        elves_moved = 0
        for target in targets:
            if len(targets[target]) > 1:
                continue
            self.elves -= {targets[target][0]}
            self.elves |= {target}

            elves_moved += 1

            i, j = target
            (min_i, min_j), (max_i, max_j) = self.boundaries
            self.boundaries = (min(min_i, i), min(min_j, j)), (max(max_i, i), max(max_j, j))

        return elves_moved

    def play(self, max_rounds=10):
        for i in range(max_rounds):
            if not self.round():
                break
            self.moves = self.moves[1:] + [self.moves[0]]
        return i + 1

    def score(self):
        (min_i, min_j), (max_i, max_j) = self.boundaries

        return (max_i-min_i+1) * (max_j-min_j+1) - len(self.elves)

    def __repr__(self):
        (min_i, min_j), (max_i, max_j) = self.boundaries
        lines = []
        for i in range(min_i, max_i+1):
            line = ''
            for j in range(min_j, max_j+1):
                line += '#' if (i, j) in self.elves else '.'
            lines.append(line)
        return '\n'.join(lines)


def part1():
    g = AdventuringElves()
    g.read()
    g.play(10)
    return g.score()


def part2():
    g = AdventuringElves()
    g.read()
    return g.play(10_000_000)


if __name__ == '__main__':
    print(f'Part 1:', part1())
    print(f'Part 2:', part2())
