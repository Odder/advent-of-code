from aoc.input import ints
from aoc.aoc import part1and2yield


@part1and2yield()
def solve1():
    valids = 0
    memory = []
    lines = list(ints())
    i = 0
    n = 0
    for i, n in enumerate(lines):
        memory.append(n)
        if len(memory) <= 25:
            continue
        memory_set = set(memory)

        for a in memory:
            if n - a in memory_set:
                valids += 1
                break
        else:
            yield n
            break
        memory = memory[1:]

    j = i
    while True:
        j -= 1
        contiguous_sum = sum(lines[j:i])
        if contiguous_sum > n:
            i -= 1
            j = i
        if contiguous_sum == n:
            yield min(lines[j:i]) + max(lines[j:i])


if __name__ == '__main__':
    pass
