import re
from collections import defaultdict, deque
from aoc.input import ints, lines, grouped_lines, tokens_filter, tokens_pattern
from aoc.aoc import part1, part2, part1and2, part1and2yield


@part1()
def solve1():
    memory = {}
    bit_mask = 0
    bit_override = 0
    for line in lines():
        match line.split(' = '):
            case 'mask', mask:
                bit_mask = 0
                bit_override = 0
                for bit in mask:
                    bit_mask <<= 1
                    bit_override <<= 1
                    if bit == 'X':
                        bit_mask += 1
                    if bit == '1':
                        bit_override += 1
                pass
            case cmd, val:
                addr = re.findall(r'\d+', cmd)[0]
                memory[addr] = bit_override ^ (bit_mask & int(val))
    return sum(memory.values())




@part2()
def solve2():
    memory = {}
    bit_masks = []
    bit_floating_mask = 0
    for line in lines():
        match line.split(' = '):
            case 'mask', mask:
                bit_masks = [0]
                bit_floating_mask = 0
                for bit in mask:
                    bit_floating_mask <<= 1
                    if bit == '1':
                        for i, bm in enumerate(bit_masks):
                            bit_masks[i] = (bm << 1) + 1
                    if bit == '0':
                        for i, bm in enumerate(bit_masks):
                            bit_masks[i] = (bm << 1)
                    if bit == 'X':
                        bit_floating_mask += 1
                        extension = [0] * len(bit_masks)
                        for i, bm in enumerate(bit_masks):
                            bit_masks[i] = (bm << 1)
                            extension[i] = (bm << 1) + 1
                        bit_masks.extend(extension)


                pass
            case cmd, val:
                addr = int(re.findall(r'\d+', cmd)[0])
                for bit_mask in bit_masks:
                    new_addr = addr & (~bit_floating_mask) | bit_mask
                    memory[new_addr] = int(val)
    return sum(memory.values())


@part1and2()
def solve():
    return 0, 0


@part1and2yield()
def solve4():
    yield 0
    yield 0


def examples():
    for line in lines():
        pass

    for group in grouped_lines():
        for line in group:
            pass

    for key, value in tokens_pattern(regex=r'(\d+): (.+)'):
        pass

if __name__ == '__main__':
    pass
