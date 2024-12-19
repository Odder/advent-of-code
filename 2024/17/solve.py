from aoc.input import lines, nums
from aoc.aoc import part1and2yield

@part1and2yield()
def solve1():
    l = list(lines())
    inp = nums(l[4])
    a = nums(l[0])[0]

    def run(program, r_a, r_b=0, r_c=0):
        out = []
        i = 0
        while i < len(program):
            opcode = program[i]
            operand = program[i + 1]
            i += 2
            combo = operand if operand < 4 else [r_a, r_b, r_c][operand - 4]

            match opcode:
                case 0:
                    r_a //= 1 << combo
                case 1:
                    r_b ^= operand
                case 2:
                    r_b = combo & 7
                case 3 if r_a != 0:
                    i = operand
                case 4:
                    r_b ^= r_c
                case 5:
                    out.append(combo & 7)
                case 6:
                    r_b = r_a // (1 << combo)
                case 7:
                    r_c = r_a // (1 << combo)
        return out

    yield run(inp, a)

    k = 872694763117 # 7 -> 12 -> 15
    while True:
        k += 1073741824
        out = run(inp, k)
        if out == inp:
            yield k

if __name__ == '__main__':
    pass
