import re
from collections import deque


class Grove:
    def __init__(self, zones=None):
        self.map = []
        self.portals = {}
        self.direction = 0
        self.width = 0
        self.height = 0
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.instructions = deque([])
        self.pos = (0, 0)
        self.zones = zones

    def read(self):
        with open('input', 'r') as file:
            for i, line in enumerate(file):
                line = line.strip('\n')
                if line.strip() == '':
                    break

                self.map.append(list(line))
                self.width = max(len(line), self.width)
            line = file.readline().strip()
            steps = list(map(int, re.findall('\d+', line)))
            turns = re.findall('[RL]', line)
            turns += [''] if len(steps) > len(turns) else []
            self.instructions = deque(zip(steps, turns))
        self.height = len(self.map)
        for line in self.map:
            line += [' '] * (self.width - len(line))
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == '.':
                    self.pos = i, j
                    return self

        raise 'No starting position found'

    def move(self):
        steps, turn = self.instructions.popleft()
        for _ in range(steps):
            x, y = self.pos
            delta_x, delta_y = self.directions[self.direction]
            dir = self.direction
            x, y = x + delta_x, y + delta_y
            if x // 50 != (x - delta_x) // 50 or y // 50 != (y - delta_y) // 50:
                a = ((x - delta_x) // 50, (y - delta_y) // 50)
                wrap = self.zones[a][dir]
                (x, y), dir = wrap(x - delta_x, y - delta_y)
                x, y = x + self.directions[dir][0], y + self.directions[dir][1]
            if self.map[x][y] == '#':
                break
            self.pos = x, y
            self.direction = dir

        self.direction += 1 if turn == 'R' else 0
        self.direction += 3 if turn == 'L' else 0
        self.direction %= 4

    def play(self):
        k = 0
        while self.instructions:
            k+=1
            self.move()

        return self

    def score(self):
        x, y = self.pos
        return (x+1) * 1000 + (y+1) * 4 + self.direction

    def __repr__(self):
        lines = []
        x, y = self.pos
        for i, line in enumerate(self.map):
            line = line[:]
            if i == x:
                line[y] = '>V<^'[self.direction]
            lines.append(''.join(line))
        return '\n'.join(lines)


def part1():
    zones = {
        (0, 1): [
            lambda x, y: ((x, y), 0),
            lambda x, y: ((x, y), 1),
            lambda x, y: ((x, y + 100), 2),
            lambda x, y: ((x + 150, y), 3),
        ],
        (0, 2): [
            lambda x, y: ((x, y - 100), 0),
            lambda x, y: ((x - 50, y), 1),
            lambda x, y: ((x, y), 2),
            lambda x, y: ((x + 50, y), 3),
        ],
        (1, 1): [
            lambda x, y: ((x, y - 50), 0),
            lambda x, y: ((x, y), 1),
            lambda x, y: ((x, y + 50), 2),
            lambda x, y: ((x, y), 3),
        ],
        (2, 1): [
            lambda x, y: ((x, y - 100), 0),
            lambda x, y: ((x - 150, y), 1),
            lambda x, y: ((x, y), 2),
            lambda x, y: ((x, y), 3),
        ],
        (2, 0): [
            lambda x, y: ((x, y), 0),
            lambda x, y: ((x, y), 1),
            lambda x, y: ((x, y + 100), 2),
            lambda x, y: ((x + 100, y), 3),
        ],
        (3, 0): [
            lambda x, y: ((x, y - 50), 0),
            lambda x, y: ((x - 100, y), 1),
            lambda x, y: ((x, y + 50), 2),
            lambda x, y: ((x, y), 3),
        ],
    }

    g = Grove(zones=zones)
    g.read()
    g.play()
    return g.score()


def part2():
    zones = {
            (0, 1): [
                lambda x, y: ((x, y), 0),        # 2
                lambda x, y: ((x, y), 1),        # 3
                lambda x, y: ((149 - x, -1), 0),  # 5
                lambda x, y: ((100 + y, -1), 0),   # 6
            ],
            (0, 2): [
                lambda x, y: ((149 - x, 100), 2),  # 4
                lambda x, y: ((y - 50, 100), 2),   # 3
                lambda x, y: ((x, y), 2),        # 1
                lambda x, y: ((200, y - 100), 3), # 6
            ],
            (1, 1): [
                lambda x, y: ((50, 50 + x), 3),   # 2
                lambda x, y: ((x, y), 1),       # 4
                lambda x, y: ((99, x - 50), 1),  # 5
                lambda x, y: ((x, y), 3),        # 1
            ],
            (2, 1): [
                lambda x, y: ((149 - x, 150), 2), # 2
                lambda x, y: ((y + 100, 50), 2),  # 6
                lambda x, y: ((x, y), 2),        # 5
                lambda x, y: ((x, y), 3),        # 3
            ],
            (2, 0): [
                lambda x, y: ((x, y), 0),        # 4
                lambda x, y: ((x, y), 1),       # 6
                lambda x, y: ((149 - x, 49), 0),  # 1
                lambda x, y: ((y + 50, 49), 0),   # 3
            ],
            (3, 0): [
                lambda x, y: ((150, x - 100), 3), # 4
                lambda x, y: ((0, 100 + y), 1),   # 2
                lambda x, y: ((0, x - 100), 1),   # 1
                lambda x, y: ((x, y), 3),       # 5
            ],
        }
    g = Grove(zones=zones)
    g.read()
    g.play()
    return g.score()


if __name__ == '__main__':
    print(f'Part 1:', part1())
    print(f'Part 2:', part2())
