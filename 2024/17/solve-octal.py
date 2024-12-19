from aoc.input import lines, nums
from aoc.aoc import part1and2yield
from algs.search import BFS

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

    kk = 1
    for q, num, match in BFS((0, 0)):
        print(kk, oct(num))
        kk+=1
        for k in range(8):
            cand = num*8 + k
            res = run(inp, cand)
            if res == inp[-len(res):]:
                if len(res) == len(inp):
                    yield cand
                    break
                q.append((cand, len(res)))

if __name__ == '__main__':
    pass
