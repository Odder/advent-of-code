from aoc.input import lines
from aoc.aoc import part1and2yield

def search(cb):
    i = 0
    acc = 0
    seen = set()
    while i < len(cb):
        if i in seen:
            return acc, False
        seen |= {i}
        match cb[i]:
            case ('acc', offset):
                acc += offset
                i += 1
            case ('jmp', offset):
                i += offset
            case ('nop', _):
                i += 1
    return acc, True


@part1and2yield()
def solve1():
    codebase = []
    for line in lines():
        a, b = line.split(' ')
        codebase.append((a, int(b)))

    yield search(codebase)[0]

    for i, line in enumerate(codebase):
        cp_cb = codebase[:]
        match line:
            case('jmp', offset):
                cp_cb[i] = ('nop', offset)
            case('nop', offset):
                cp_cb[i] = ('jmp', offset)
            case _:
                continue
        acc, terminated = search(cp_cb)
        if terminated:
            yield acc
            break

if __name__ == '__main__':
    pass
