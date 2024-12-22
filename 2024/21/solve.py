from functools import cache
from itertools import pairwise, permutations, product
from algs.spaces.imaginary_s2 import load_grid
from aoc.input import lines
from aoc.aoc import part1, part2

pad1 = load_grid(['789', '456', '123', 'X0A'])
idx1 = {pad1[p]: p for p in pad1.keys()}
pad2 = load_grid(['X^A', '<v>'])
idx2 = {pad2[p]: p for p in pad2.keys()}
moves = {'^': -1, '<': -1j, 'v': 1, '>': 1j}
moves_map = {v: k for k, v in moves.items()}

@cache
def get_paths_between(a, b, is_pad2=True):
    pad = pad2 if is_pad2 else pad1
    idx = idx2 if is_pad2 else idx1
    p = idx[a]
    v = idx[b] - p
    paths = []
    moves = [1] * int(v.real) + [-1] * int(-v.real) + [1j] * int(v.imag) + [-1j] * int(-v.imag)
    for path in set(permutations(moves)):
        d = 0
        for move in path:
            d += move
            if pad[p + d] == 'X':
                break
        else:
            paths.append([moves_map[x] for x in path])
    return [''.join(x) for x in paths]

@cache
def get_paths(substr, is_pad2=True):
    parts = []
    for a, b in pairwise('A' + substr):
        parts.extend([get_paths_between(a, b, is_pad2), ['A']])
    return [''.join(x) for x in product(*parts)]

@cache
def min_length(s, rounds=2, is_pad2=True):
    length = 0
    parts = [x+'A' for x in s.split('A')]
    parts = parts[:-1]
    if rounds == 0:
        return len(get_paths(s, is_pad2)[0])
    for part in parts:
        if rounds == 0:
            length += len(get_paths(part, is_pad2)[0])
        else:
            length += min(min_length(x, rounds-1) for x in get_paths(part, is_pad2))
    return length

@part2(25)
@part1()
def solve1(rounds=2):
    return sum(int(line[:-1], 10)*(min_length(line, rounds, False)) for line in lines())

if __name__ == '__main__':
    pass
