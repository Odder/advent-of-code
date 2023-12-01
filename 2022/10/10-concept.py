import sys
sys.path.append('C:/Users/oscar/Code/Bnanan/Python/algas/src')
from algas.input import tokens
from aoc.aoc import part1and2


class Crt:
    def __init__(self):
        self.cursor = 0
        self.score = 0
        self.buffer = 1

    def print(self):
        self.cursor += 1
        self.score += self.buffer * self.cursor if ((self.cursor + 20) % 40) == 0 else 0
        print('#' if abs(self.buffer - ((self.cursor - 1) % 40)) < 2 else ' ',
              end='' if self.cursor % 40 else '\n')


@part1and2()
def main():
    crt = Crt()
    for command in tokens():
        crt.print()
        match list(command):
            case ['addx', offset]:
                crt.print()
                crt.buffer += int(offset)

    return crt.score, 'See print above'
