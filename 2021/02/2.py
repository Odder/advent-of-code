import sys
sys.path.append('C:/Users/oscar/Code/Bnanan/Python/algas/src')
from algas.lists import top_n, group
from algas.input import tokens
from aoc.aoc import part1, part2

@part2(1)
@part1(0)
def main(flag):
    h = 0
    d = 0
    aim = 0
    for command in tokens():
        match (list(command)):
            case ['forward', x]:
                h += int(x)
                d += flag * (aim * int(x))
            case ['up', x]:
                if not flag:
                    d -= int(x)
                else:
                    aim -= int(x)
            case ['down', x]:
                if not flag:
                    d += int(x)
                else:
                    aim += int(x)

    return h*d
