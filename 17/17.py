rocks = [
    [
        [
            [1, 1, 1, 1, 0, 0, 0],
        ],
        [
            [0, 1, 1, 1, 1, 0, 0],
        ],
        [
            [0, 0, 1, 1, 1, 1, 0],
        ],
        [
            [0, 0, 0, 1, 1, 1, 1],
        ],
    ],
    [
        [
            [0, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 0],
        ],
    ],
    [
        [
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 1, 1, 0],
        ],
        [
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 1, 1],
        ],
    ],
    [
        [
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
        ],
        [
            [0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0],
        ],
        [
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
        ],
    ],
    [
        [
            [1, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0],
        ],
        [
            [0, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0],
        ],
        [
            [0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0],
        ],
        [
            [0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 0, 0],
        ],
        [
            [0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 1, 1, 0],
        ],
        [
            [0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 1, 1],
        ],
    ],
]


def translate(brick, curr, signal):
    curr += 1 if signal == '>' else -1
    curr = 0 if curr < 0 else curr
    curr = len(brick)-1 if curr == len(brick) else curr
    return curr


def read():
    with open('input', 'r') as file:
        return list(file.readline().strip())


class Tetris():
    def __init__(self):
        self.turn = 0
        self.rock = []
        self.rock_height = 0
        self.floor = 1
        self.score = 0
        self.cave = [[1] * 7] + [[0] * 7 for _ in range(100_000)]

    def spawn_rock(self):
        self.rock = rocks[self.turn % 5][2][::-1]
        self.rock_height = 3
        self.turn += 1

    def solidify_rock(self):
        for i in range(len(self.rock)):
            for j in range(7):
                row = self.floor + self.rock_height + i
                self.cave[row][j] = max(self.rock[i][j], self.cave[row][j])
        for i in range(4, -1, -1):
            for j in range(7):
                if self.cave[self.floor + i][j] == 1:
                    self.floor = self.floor + i + 1
                    return True

    def fall(self):
        for i in range(len(self.rock)):
            for j in range(7):
                if self.rock[i][j] == 1 and self.cave[self.floor + self.rock_height + i - 1][j] == 1:
                    return False

        self.rock_height -= 1
        return True

    def wind(self, op):
        offset = 1 if op == '>' else -1
        for i in range(len(self.rock)):
            for j in range(7):
                if j == 0 and offset == -1:
                    if self.rock[i][j] == 1:
                        return False
                    continue
                if j == 6 and offset == 1:
                    if self.rock[i][j] == 1:
                        return False
                    continue
                if self.rock[i][j] == 1 and self.cave[self.floor + self.rock_height + i][j + offset] == 1:
                    return False
        for i in range(len(self.rock)):
            if offset == 1:
                self.rock[i] = [0] + self.rock[i][:6]
            if offset == -1:
                self.rock[i] = self.rock[i][1:] + [0]

        return True

    def play(self, ops, turns):
        k = 0
        prev_floor = 0
        prev_turn = 0
        prev_delta = 0
        big_addition = 0
        while self.turn < turns:
            self.spawn_rock()
            while True:
                if k % len(ops) == 0:
                    if prev_delta == (self.floor - prev_floor, self.turn - prev_turn):
                        cycles_skipping = ((turns - self.turn) // (self.turn - prev_turn))
                        big_addition = cycles_skipping * (self.floor - prev_floor)
                        self.turn += cycles_skipping * (self.turn - prev_turn)
                    prev_delta = self.floor - prev_floor, self.turn - prev_turn
                    prev_floor = self.floor
                    prev_turn = self.turn

                self.wind(ops[k % len(ops)])
                k += 1
                if not self.fall():
                    break

            self.solidify_rock()
        self.score = self.floor + big_addition - 1

    def __repr__(self):
        string = ''
        for i in range(self.floor + 2, max(0, self.floor - 10), -1):
            line = ''.join('#' if x else ' ' for x in self.cave[i])
            string += f' |{line}|\n'
        return string + f' ^^^^^^^^^'


def part1():
    t = Tetris()
    t.play(read(), 2022)
    print(t)
    return t.score


def part2():
    t = Tetris()
    t.play(read(), 1_000_000_000_000)
    print(t)
    return t.score


if __name__ == '__main__':
    print(f'Part 1:', part1())
    print(f'Part 2:', part2())
